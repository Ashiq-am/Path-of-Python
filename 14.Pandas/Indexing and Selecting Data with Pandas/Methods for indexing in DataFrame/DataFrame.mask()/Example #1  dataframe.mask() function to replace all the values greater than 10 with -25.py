# replace values greater than 10 with -25
from pandas.tests.test_downstream import df

df.mask(df > 10, -25)
