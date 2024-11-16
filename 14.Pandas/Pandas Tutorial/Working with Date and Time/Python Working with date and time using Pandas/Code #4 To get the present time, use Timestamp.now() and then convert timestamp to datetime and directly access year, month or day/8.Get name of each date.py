# Get name of each date
from pandas.tests.groupby.test_value_counts import df

df.Time.dt.weekday_name.head()
