# to interpolate the missing values
from pandas.tests.groupby.test_value_counts import df

df.interpolate(method ='linear', limit_direction ='forward')

