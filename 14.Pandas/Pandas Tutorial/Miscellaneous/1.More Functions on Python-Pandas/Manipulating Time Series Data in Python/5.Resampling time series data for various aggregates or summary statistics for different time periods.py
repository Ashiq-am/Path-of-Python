# importing pandas
import pandas as pd
from datetime import datetime

# reading csv file
data = pd.read_csv('covid_data.csv')

# converting string data to datetime
data['ObservationDate'] = pd.to_datetime(data['ObservationDate'])

# setting index
data = data.set_index('ObservationDate')

# resampling data according to year
data = data.resample('Y').mean()
print(data)
