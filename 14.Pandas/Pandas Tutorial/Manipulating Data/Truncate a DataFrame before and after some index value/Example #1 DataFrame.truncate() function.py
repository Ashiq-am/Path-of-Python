# return the truncated dataframe
from pandas.tests.groupby.test_value_counts import df

result = df.truncate(before = '2010-10-09 09:45:00', after = '2010-10-09 11:45:00')

# Print the result
print(result)




"""

to truncate the entries before ‘2010-10-09 09.45.00’ and after 
‘2010-10-09 11.45.00’ in the given dataframe

"""