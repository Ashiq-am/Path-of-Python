# Calculate mean rating of all movies
from numpy.random.tests import data

data.groupby('title')['rating'].mean().sort_values(ascending=False).head()
