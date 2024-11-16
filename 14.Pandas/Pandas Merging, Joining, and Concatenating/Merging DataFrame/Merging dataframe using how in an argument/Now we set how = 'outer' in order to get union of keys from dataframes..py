# getting union  of keys
from turtle import pd

from pandas.tests.reshape.merge.test_merge_index_as_string import df1
from pandas.tests.test_downstream import df

res2 = pd.merge(df, df1, how='outer', on=['key', 'key1'])

res2