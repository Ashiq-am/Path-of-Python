# importing pandas
import pandas as pd

# reading csv file
data = pd.read_csv('covid_data.csv')

# converting string data to datetime
data['ObservationDate'] = pd.to_datetime(data['ObservationDate'])

# setting index
data = data.set_index('ObservationDate')
print(data.head())

# indexing and slicing through the dataframe
print(data.loc['2020-01-22'][:10])
