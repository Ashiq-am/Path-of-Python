from turtle import pd

from pandas.tests.test_downstream import df

data = pd.merge(df, movie_titles, on='item_id')
data.head()
