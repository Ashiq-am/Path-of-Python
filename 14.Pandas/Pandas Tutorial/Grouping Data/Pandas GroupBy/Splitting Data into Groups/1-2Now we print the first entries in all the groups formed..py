# applying groupby() function to
# group the data on Name value.
from pandas.tests.groupby.test_value_counts import df

gk = df.groupby('Name')

# Let's print the first entries
# in all the groups formed.
gk.first()
