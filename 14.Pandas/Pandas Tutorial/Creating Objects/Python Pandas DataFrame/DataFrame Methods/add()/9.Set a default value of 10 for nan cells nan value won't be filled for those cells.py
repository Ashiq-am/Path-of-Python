# Set a default value of 10 for nan cells
# nan value won't be filled for those cells
# in which both data frames has nan value
from pandas.tests.groupby.test_value_counts import df
from pandas.tests.reshape.merge.test_merge_index_as_string import df2

df.add(df2, fill_value = 10)
