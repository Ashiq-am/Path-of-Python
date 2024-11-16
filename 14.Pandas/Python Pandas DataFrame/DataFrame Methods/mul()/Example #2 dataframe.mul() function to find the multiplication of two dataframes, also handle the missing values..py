# fill the missing values with 100
from pandas.tests.reshape.merge.test_merge_index_as_string import df2, df1

df1.mul(df2, fill_value = 100)
