# importing pandas
import pandas as pd
from datetime import datetime

# reading csv file
data = pd.read_csv('covid_data.csv')

# converting string data to datetime
data['ObservationDate'] = pd.to_datetime(data['ObservationDate'])

# setting index
data = data.set_index('ObservationDate')

# indexing and slicing through the dataframe
print(data.loc['2020-01-22':'2020-02-22'])
