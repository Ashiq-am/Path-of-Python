# importing pandas module for data frame
import pandas as pd

# creating data frame for different customers
# in a shop with respect to dates
data = pd.DataFrame({'dates': ['1/2/2021',
							'2/4/2020',
							'1/3/2021',
							'4/12/2017'],
					'customers': [100, 30, 56, 56]})

# display original data
data

# converting dates column to date
# using pandas.to_datetime function
data['dates'] = pd.to_datetime(data['dates'])

# data after conversion
data
