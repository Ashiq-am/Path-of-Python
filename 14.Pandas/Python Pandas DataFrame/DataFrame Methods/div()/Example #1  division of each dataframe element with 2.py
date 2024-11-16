# Find the division with 50 being substituted
# for all the missing values in the dataframe
from pandas.tests.groupby.test_value_counts import df

df.div(2, fill_value = 50)
