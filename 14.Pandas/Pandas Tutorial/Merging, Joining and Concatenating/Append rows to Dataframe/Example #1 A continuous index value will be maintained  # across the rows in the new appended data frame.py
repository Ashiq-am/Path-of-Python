# A continuous index value will be maintained
# across the rows in the new appended data frame.
from pandas.tests.reshape.merge.test_merge_index_as_string import df2

df1.append(df2, ignore_index = True)
