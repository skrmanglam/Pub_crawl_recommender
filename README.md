# Pub_crawl_recommender
Recommender system built on top of travelling sales man problem.

* Shortest Path algoritm:
Uses Djkstra's algorithm
Catculates shortest path given a set of point on the map using Open street maps. (OSMNX)
Outputs a ordered list of the Pub names and the total distance.

* GUI
Takes a ordered list and produces a Map as an image. This can be switched to Gmap's api.

* Recommender System:
take location and radius as input.
Create a database of all the pub-reviews
In that database perform NLP to recommend pubs and also the buzz words.
Should output a dictionary in order of recommendation and buzz words tagged.
