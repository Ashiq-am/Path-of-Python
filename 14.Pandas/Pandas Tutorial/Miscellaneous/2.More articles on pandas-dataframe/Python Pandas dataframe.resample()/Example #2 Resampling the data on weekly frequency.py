# importing pandas as pd
import pandas as pd

# We know that resampling works with time-series data
# only so convert "date" column to index
# index_col ="date", makes "date" column.

df = pd.read_csv("apple.csv", parse_dates =["date"], index_col ="date")

# Resampling the time series data based on weekly frequency
# we apply it on stock open price 'W' indicates week
weekly_resampled_data = df.open.resample('W').mean()

# find the mean opening price of each week
# for each week over a period of 1 year.
weekly_resampled_data
