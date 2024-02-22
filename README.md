# Hybrid recommendation system for Chicago restaurants.

The implementation is located in the file *RS_chicago_restaurants/RS_restaurant.ipynb*, here you will find three systems:

1. Content based filter
2. User based content filter
	1. it was built using MiniBatchKmeans from sklearn library.
3. Item based content filter (Item2vec)
	1. it was built using Gensim library, which is a useful library for word embedding processes (an NLP technique).

The above filters work well when mixed together because of their complementary strengths and weaknesses

## Remarks:

- Evaluation of precision and recall is not implemented.
- Resources paths are absolute (it won't work out of the box).

# Data
[Entree Chicago restaurant](https://archive.ics.uci.edu/dataset/123/entree+chicago+recommendation+data)

