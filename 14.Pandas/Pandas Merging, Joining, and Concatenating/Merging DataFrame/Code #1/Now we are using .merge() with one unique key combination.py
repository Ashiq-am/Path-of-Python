# using .merge() function
from turtle import pd

from pandas.tests.reshape.merge.test_merge_index_as_string import df1
from pandas.tests.test_downstream import df

res = pd.merge(df, df1, on='key')

res