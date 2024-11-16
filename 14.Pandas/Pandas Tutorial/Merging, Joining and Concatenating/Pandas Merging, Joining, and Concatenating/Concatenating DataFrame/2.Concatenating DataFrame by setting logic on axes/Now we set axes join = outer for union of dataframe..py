# using a .concat for
# union of dataframe
from turtle import pd

from pandas.tests.reshape.merge.test_merge_index_as_string import df1
from pandas.tests.test_downstream import df

res2 = pd.concat([df, df1], axis=1, sort=False)

res2