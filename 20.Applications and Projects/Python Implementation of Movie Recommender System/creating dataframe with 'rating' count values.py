# creating dataframe with 'rating' count values
from turtle import pd

from numpy.random.tests import data

ratings = pd.DataFrame(data.groupby('title')['rating'].mean())

ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())

ratings.head()
