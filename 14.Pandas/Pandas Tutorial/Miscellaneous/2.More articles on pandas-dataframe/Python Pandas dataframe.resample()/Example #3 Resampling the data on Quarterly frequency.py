# importing pandas as pd
import pandas as pd

# We know that resampling works with time-series
# data only so convert our "date" column to index
# index_col ="date", makes "date" column
df = pd.read_csv("apple.csv", parse_dates =["date"], index_col ="date")

# Resampling the time series data
# based on Quarterly frequency
# 'Q' indicates quarter

Quarterly_resampled_data = df.open.resample('Q').mean()

# mean opening price of each quarter
# over a period of 1 year.
Quarterly_resampled_data
