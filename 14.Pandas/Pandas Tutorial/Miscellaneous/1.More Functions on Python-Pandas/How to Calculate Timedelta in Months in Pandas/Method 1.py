# import packages and libraries
import pandas as pd

# reading the csv file
data = pd.read_csv('time.csv')

# converting columns to datetime
data['start_date'] = pd.to_datetime(data['start_date'])
data['end_date'] = pd.to_datetime(data['end_date'])

# calculating time delta in months
data['time_delta_months'] = data['end_date'].dt.to_period('M') - \
	data['start_date'].dt.to_period('M')
print(data)
