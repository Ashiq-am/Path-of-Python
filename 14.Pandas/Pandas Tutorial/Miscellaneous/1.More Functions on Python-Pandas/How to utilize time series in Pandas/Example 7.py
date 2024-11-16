# importing pandas module for data frame
import pandas as pd

# creating data frame for different customers
# in a shop with respect to dates
data = pd.DataFrame({'dates': ['1/2/2021', '2/4/2020',
							'1/3/2021', '4/12/2017',
							'1/2/2021', '2/4/2020',
							'1/3/2021'],
					'customers': [100, 30, 56,
								56, 23, 45, 67]})
# display original data
data

# converting dates column to date
# using pandas.to_datetime function
data['dates'] = pd.to_datetime(data['dates'])

# after conversion
data

# finding unique time series data
print(data['dates'].nunique())

# counting each series data
data['dates'].value_counts()
