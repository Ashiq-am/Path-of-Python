# import pandas library
import pandas as pd

# create a series of date strings
dt_series = pd.Series(['28 July 2020', '2013-01-16',
					'20160229 18:14', '5/03/2019 2215',
					'20151204 09:23'])

# display the series initially
print("Series of date strings:")
print(dt_series)

# display the series after
# being converted to a time series
print("\nSeries of date strings after " +
	"being converted to a timeseries:")

print(pd.to_datetime(dt_series))
