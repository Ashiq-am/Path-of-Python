# Even if we do not specify axis = 0,
# the method will return the mean over
# the index axis by default
from pandas.tests.groupby.test_value_counts import df

df.mean(axis = 0)
