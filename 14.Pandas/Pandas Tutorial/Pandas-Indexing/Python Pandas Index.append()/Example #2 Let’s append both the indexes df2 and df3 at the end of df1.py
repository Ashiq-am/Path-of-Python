# We pass df2 and df3 as a list of
# indexes to the append function
from pandas.tests.reshape.merge.test_merge_index_as_string import df2

df1.append([df2, df3])
