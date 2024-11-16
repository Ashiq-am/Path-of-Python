# applying a function by passing
# a list of functions
from pandas import np
from pandas.tests.groupby.test_value_counts import df

grp = df.groupby('Name')

grp['Age'].agg([np.sum, np.mean, np.std])
