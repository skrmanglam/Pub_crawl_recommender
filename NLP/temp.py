# Import necessary libraries
import pandas as pd
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
from sentence_transformers import SentenceTransformer
import pinecone
from tqdm.auto import tqdm

# Load and preprocess data
df = pd.read_excel("night_clubs_data.xlsx")  # Assuming reviews are already extracted and saved

# Load a sentence transformer model for embeddings
model_name = 'sentence-transformers/all-MiniLM-L6-v2'
sentence_model = SentenceTransformer(model_name)

# Function to embed reviews
def embed_reviews(df):
    df['embeddings'] = df['Review'].apply(lambda x: sentence_model.encode(x))
    return df

# Embed reviews in the DataFrame
df_embedded = embed_reviews(df)

# Initialize Pinecone (Assuming Pinecone and Pinecone Index are already set up)
pinecone.init(api_key='YOUR_PINECONE_API_KEY', environment='us-west1-gcp')
index_name = 'pub-crawl-recommender'
# Check if the index exists, if not create one
if index_name not in pinecone.list_indexes():
    pinecone.create_index(name=index_name, dimension=model.get_sentence_embedding_dimension())

# Connect to the Pinecone index
index = pinecone.Index(index_name)

# Function to upload embeddings to Pinecone
def upload_embeddings_to_pinecone(df):
    for i in tqdm(range(0, len(df), 50)):
        batch = df.iloc[i:i+50]
        vectors = [(str(row['Club Name']), row['embeddings'].tolist()) for index, row in batch.iterrows()]
        index.upsert(vectors=vectors)

# Upload embeddings
upload_embeddings_to_pinecone(df_embedded)

# Example query function
def query_pubs(query, top_k=5):
    query_embedding = sentence_model.encode(query)
    query_results = index.query([query_embedding.tolist()], top_k=top_k)
    return query_results

# Example usage
query = "I'm looking for a pub with great ambiance and craft beers."
results = query_pubs(query)
print(results)
