import pandas as pd
from pandas import DataFrame

# creating a dictionary of Dates
Dates = {'Day': [1, 29, 23, 4, 15],
		'Month': ['Aug', 'Feb', 'Aug', 'Apr', 'Mar'],
		'Year': [1947, 1983, 2007, 2011, 2020]}

# creating a dataframe from dictionary
df = DataFrame(Dates, columns = ['Day', 'Month', 'Year'])
print (df)

print('\n')

# concatenating the columns
df['Date'] = df['Day'].map(str) + '-' + df['Month'].map(str) + '-' + df['Year'].map(str)
print (df)
