# using groupby function
# with sort
from pandas.tests.groupby.test_value_counts import df

df.groupby(['Name'], sort = False).sum()
