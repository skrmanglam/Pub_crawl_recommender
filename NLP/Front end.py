"""Using streamlit to design and deploy front end in the webbrowser for the chatbot"""
# Front end.py
# Functionality: Use Streamlit for front-end deployment

import streamlit as st


# Function to display the front end and handle user interactions
def display_front_end():
    st.title("Pub Crawl Recommender")

    user_query = st.text_input("Enter your preferences to find the best pubs for you:")

    if st.button("Recommend Pubs"):
        if user_query:
            # Placeholder for the function that handles the query and returns results
            results = query_pubs(user_query)  # Implement this function based on temp.py
            st.write(results)
        else:
            st.write("Please enter your preferences to get recommendations.")


if __name__ == "__main__":
    display_front_end()
