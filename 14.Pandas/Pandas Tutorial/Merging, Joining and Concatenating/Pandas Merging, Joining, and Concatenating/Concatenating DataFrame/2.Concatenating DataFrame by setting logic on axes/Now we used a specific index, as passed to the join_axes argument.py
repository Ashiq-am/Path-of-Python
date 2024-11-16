# using join_axes
from turtle import pd

from pandas.tests.reshape.merge.test_merge_index_as_string import df1

res3 = pd.concat([df, df1], axis=1, join_axes=[df.index])

res3