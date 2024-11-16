# We have given a default value
# of '10' for all the nan cells
from pandas.tests.groupby.test_value_counts import df

df.add(1, fill_value = 10)
