# drop all those rows which
# have any 'nan' value in it.
from pandas.tests.groupby.test_value_counts import df

df.dropna(inplace = True)
