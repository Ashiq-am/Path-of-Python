# using transform function
from pandas.tests.groupby.test_value_counts import df

grp = df.groupby('Name')
sc = lambda x: (x - x.mean()) / x.std()*10
grp.transform(sc)
