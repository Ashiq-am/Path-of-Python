# find standard error of the mean of all the columns
from pandas.tests.groupby.test_value_counts import df

df.sem(axis = 0)
