# using a .concat() method
from turtle import pd

from pandas.tests.reshape.merge.test_merge_index_as_string import df1
from pandas.tests.test_downstream import df

frames = [df, df1]

res1 = pd.concat(frames)
res1