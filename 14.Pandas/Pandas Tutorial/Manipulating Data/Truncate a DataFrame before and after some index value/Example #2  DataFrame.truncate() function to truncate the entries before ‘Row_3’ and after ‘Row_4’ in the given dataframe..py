# return the truncated dataframe
from pandas.tests.groupby.test_value_counts import df

result = df.truncate(before = 'Row_3', after = 'Row_4')

# Print the result
print(result)
