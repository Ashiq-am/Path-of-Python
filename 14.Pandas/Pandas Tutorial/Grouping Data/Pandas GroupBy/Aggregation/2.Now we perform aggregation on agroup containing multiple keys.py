# performing aggregation on
# group containing multiple
# keys
from pandas.tests.groupby.test_value_counts import df

grp1 = df.groupby(['Name', 'Qualification'])

grp1.aggregate(np.sum)
