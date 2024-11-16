# equivalent to df - sr
from pandas.tests.groupby.test_value_counts import df

df.sub(sr, axis = 1)
