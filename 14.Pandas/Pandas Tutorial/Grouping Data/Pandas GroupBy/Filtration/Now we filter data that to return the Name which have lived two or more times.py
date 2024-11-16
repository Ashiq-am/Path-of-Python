# filtering data using
# filter data
from pandas.tests.groupby.test_value_counts import df

grp = df.groupby('Name')
grp.filter(lambda x: len(x) >= 2)
