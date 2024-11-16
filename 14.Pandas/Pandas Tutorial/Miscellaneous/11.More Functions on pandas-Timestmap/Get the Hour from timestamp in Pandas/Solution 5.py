# importing the module
import pandas as pd

# read the date from xyz.csv file
frame = pd.read_csv(r'xyz.csv')
print("Values in xyz.csv: ")
print(frame.head())

frame['dateTime'] = frame['dateTime'].astype('datetime64[ns]')

# extract Hours from Timestamp
print("Hours: ")
print(frame.dateTime.dt.hour.head())
