# performing aggregation using
# aggregate method
from pandas.tests.groupby.test_value_counts import df

grp1 = df.groupby('Name')

grp1.aggregate(np.sum)
