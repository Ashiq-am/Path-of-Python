# using keys from left frame
from turtle import pd

from pandas.tests.reshape.merge.test_merge_index_as_string import df1
from pandas.tests.test_downstream import df

res = pd.merge(df, df1, how='left', on=['key', 'key1'])

res