# using groupby function
# without using sort
from pandas.tests.groupby.test_value_counts import df

df.groupby(['Name']).sum()
