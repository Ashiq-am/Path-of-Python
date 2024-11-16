# importing pandas
import pandas as pd
from datetime import datetime

# reading csv file
data = pd.read_csv('covid_data.csv')

# converting string data to datetime
data['ObservationDate'] = pd.to_datetime(data['ObservationDate'])
data['Last Update'] = pd.to_datetime(data['Last Update'])

# setting index
data = data.set_index('ObservationDate')

data = data[['Last Update', 'Confirmed']]
data['rolling_sum'] = data.rolling(5).sum()
print(data.head())

# dealing with missing data
data['rolling_backfilled'] = data['rolling_sum'].fillna(method='backfill')
print(data.head(5))
