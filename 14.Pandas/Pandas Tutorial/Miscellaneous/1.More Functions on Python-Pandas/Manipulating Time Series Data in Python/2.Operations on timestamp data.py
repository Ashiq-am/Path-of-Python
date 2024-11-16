# importing pandas
import pandas as pd

# creating a date range
Date_range = pd.date_range(start='1/12/2020', end='20/5/2021', freq='M')

# creating a Dataframe
Data = pd.DataFrame(Date_range, columns=['Date'])

# converting the column to datetime
Data['Date'] = pd.to_datetime(Data['Date'])
print(Data.info())
