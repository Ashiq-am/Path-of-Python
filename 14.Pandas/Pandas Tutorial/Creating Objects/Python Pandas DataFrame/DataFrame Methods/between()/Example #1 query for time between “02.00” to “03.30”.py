# Find the row values between time "02:00" to "03:30"
from pandas.tests.groupby.test_value_counts import df

df.between_time('02:00', '03:30')
