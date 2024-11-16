# importing the module
import pandas as pd

# input the timestamp
date = pd.Timestamp(year = 2020, month = 7, day = 21,
					hour = 6, minute = 30, second = 44,
					tz = 'Asia / Kolkata')
print("Timestamp: ", date)

# extract the Hours from the timestamp
print("Hour: ", date.hour)
