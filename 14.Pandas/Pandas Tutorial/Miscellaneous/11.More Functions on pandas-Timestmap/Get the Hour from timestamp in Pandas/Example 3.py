# importing the module
import pandas as pd

# take input Dates in a range
dates = pd.Series(pd.date_range('2019-8-5 10:23:05', periods = 6, freq ='H'))

# convert in a dict container
frame = pd.DataFrame(dict(givenDate = dates))

# extract Hours from Timestamp
frame['hourOfTimestamp'] = frame['givenDate'].dt.hour
print(frame)
