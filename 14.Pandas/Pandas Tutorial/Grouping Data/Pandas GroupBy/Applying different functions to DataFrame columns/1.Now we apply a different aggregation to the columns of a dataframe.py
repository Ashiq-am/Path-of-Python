# using different aggregation
# function by passing dictionary
# to aggregate
from pandas.tests.groupby.test_value_counts import df

grp = df.groupby('Name')

grp.agg({'Age' : 'sum', 'Score' : 'std'})
