# Using multiple keys in
# groupby() function
from pandas.tests.groupby.test_value_counts import df

df.groupby(['Name', 'Qualification'])

print(df.groupby(['Name', 'Qualification']).groups)
