# merging dataframe using multiple keys
from turtle import pd

from pandas.tests.reshape.merge.test_merge_index_as_string import df1
from pandas.tests.test_downstream import df

res1 = pd.merge(df, df1, on=['key', 'key1'])

res1