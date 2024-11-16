# import pandas library
import pandas as pd

# create a series of date strings
dt_series = pd.Series(['28 July 2020', '16 January 2013',
					'29 February 2016 18:14'])

# display the series initially
print("Series of date strings:")
print(dt_series)

# display the series after being
# converted to a time series
print("\nSeries of date strings after" +
	" being converted to a timeseries:")

print(pd.to_datetime(dt_series))
