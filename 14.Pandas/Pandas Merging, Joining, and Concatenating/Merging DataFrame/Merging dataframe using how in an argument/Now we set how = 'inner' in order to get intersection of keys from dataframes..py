# getting intersection of keys
from turtle import pd

from pandas.tests.reshape.merge.test_merge_index_as_string import df1
from pandas.tests.test_downstream import df

res3 = pd.merge(df, df1, how='inner', on=['key', 'key1'])

res3