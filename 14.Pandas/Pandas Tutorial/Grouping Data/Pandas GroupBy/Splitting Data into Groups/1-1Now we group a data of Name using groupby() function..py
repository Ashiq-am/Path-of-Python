# using groupby function
# with one key
from pandas.tests.groupby.test_value_counts import df

df.groupby('Name')
print(df.groupby('Name').groups)
