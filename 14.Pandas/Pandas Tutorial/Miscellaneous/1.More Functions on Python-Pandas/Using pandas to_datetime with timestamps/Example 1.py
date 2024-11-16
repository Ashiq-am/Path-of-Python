# import packages
import pandas as pd

# creating a dataframe from the csv file
data = pd.DataFrame(pd.read_csv('timestamps.csv'))

# viewing our dataframe
print("Original dataframe")
display(data)

# unit='s' to convert it into epoch time
data['Datetime'] = pd.to_datetime(data['timestamps'],
								unit='s')

# checking our dataframe once again
print("Timestamps")
display(data)
