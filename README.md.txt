
# Hybrid recommendation system for Chicago restaurants.

The implementation could be find at *RS_restaurants.ipynb*, at this Jupyter notebook you will observe the next three systems in order:

1. Content based filter
2. User based content filter
	1. it was constructed using MiniBatchKmeans from sklearn library.
3. Item based content filter (Item2vec)
	1. it was constructed using Gensim library that is an useful library for word embedding process (an NLP technique).

The objective with mixing this three methods is complement their strenghts to strengthen their own singular weakness.

## Remarks:

- The implementation of precision and recall, should be implemented.
- Paths are in absolute format.

# Data
[link](https://archive.ics.uci.edu/dataset/123/entree+chicago+recommendation+data)
<a href="https://archive.ics.uci.edu/dataset/123/entree+chicago+recommendation+data">link</a>