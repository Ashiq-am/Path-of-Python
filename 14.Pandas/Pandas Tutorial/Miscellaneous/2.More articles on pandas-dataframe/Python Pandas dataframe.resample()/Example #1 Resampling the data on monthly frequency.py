# importing pandas as pd
import pandas as pd

# By default the "date" column was in string format,
# we need to convert it into date-time format

# parse_dates =["date"], converts the "date"
# column to date-time format. We know that
# resampling works with time-series data only
# so convert "date" column to index

# index_col ="date", makes "date" column, the index of the data frame
df = pd.read_csv("apple.csv", parse_dates =["date"], index_col ="date")

# Printing the first 10 rows of dataframe
df[:10]
