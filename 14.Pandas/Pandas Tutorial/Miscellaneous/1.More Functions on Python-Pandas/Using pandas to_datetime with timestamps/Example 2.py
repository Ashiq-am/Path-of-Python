# import packages
import pandas as pd
import datetime

# creating a dataframe from the csv file
data = pd.DataFrame(pd.read_csv('timestamps.csv'))

# unit='s' to convert it into epoch time
data['Datetime'] = pd.to_datetime(data['timestamps'],
								unit='s')

data['Modified Datetime'] = data['Datetime'].dt.strftime('%d-%m-%Y %H:%M')

# checking our dataframe once again
display(data)
