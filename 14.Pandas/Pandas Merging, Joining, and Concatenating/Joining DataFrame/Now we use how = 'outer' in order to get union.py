# getting union
from pandas.tests.groupby.test_value_counts import df
from pandas.tests.reshape.merge.test_merge_index_as_string import df1

res1 = df.join(df1, how='outer')

res1