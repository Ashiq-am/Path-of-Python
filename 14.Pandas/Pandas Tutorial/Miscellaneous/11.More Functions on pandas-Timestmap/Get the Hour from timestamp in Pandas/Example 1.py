# importing the module
import pandas as pd

# input current timestamp
date = pd.Timestamp.now()
print("currentTimestamp: ", date)

# extract the Hours from the timestamp
frame = date.hour
print("Hour: ", frame)
