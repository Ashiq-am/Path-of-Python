# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series([19.5, 16.8, 22.78, 20.124, 18.1002])

# Create the Datetime Index
didx = pd.DatetimeIndex(start ='2014-08-01 10:00', freq ='W',
					periods = 5, tz = 'Asia/Calcutta')

# set the index
sr.index = didx

# Print the series
print(sr)
