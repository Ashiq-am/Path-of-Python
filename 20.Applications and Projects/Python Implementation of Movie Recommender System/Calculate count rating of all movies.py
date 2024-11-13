# Calculate count rating of all movies
from numpy.random.tests import data

data.groupby('title')['rating'].count().sort_values(ascending=False).head()
