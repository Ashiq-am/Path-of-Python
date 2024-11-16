# importing the module
import pandas as pd

# take inputs
dates = pd.Series(['2015-01-11 09:20', '2019-4-8 11:31', '2018-12-22 10:10',
				'2011-4-2 04:25', '2017-1-6 03:51'])

# give a Name to the series
seriesName = ['T1', 'T2', 'T3', 'T4', 'T5']

# give index to each timestamp
dates.index = seriesName

dates = pd.to_datetime(dates)

# extract Hours from Timestamp
rs = dates.dt.hour
print(rs)
