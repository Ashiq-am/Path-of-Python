import pandas as pd
from pandas import DataFrame

# creating a dictionary of Dates
Dates = {'Day': [1, 1, 1, 1],
		'Month': ['Jan', 'Jan', 'Jan', 'Jan'],
		'Year': [2017, 2018, 2019, 2020]}

# creating a dataframe from dictionary
df1 = DataFrame(Dates, columns = ['Day', 'Month', 'Year'])

# creating a dictionary of Rates
Rates = {'GDP': [5.8, 7.6, 5.6, 4.1],
		'Inflation Rate': [2.49, 4.85, 7.66, 6.08]}

# creating a dataframe from dictionary
df2 = DataFrame(Rates, columns = ['GDP', 'Inflation Rate'])

# combining columns of df1 and df2
df_combined = df1['Day'].map(str) + '-' + df1['Month'].map(str) + '-' + df1['Year'].map(str) + ': ' + 'GDP: ' + df2['GDP'].map(str) + '; ' + 'Inflation: ' + df2['Inflation Rate'].map(str)
print (df_combined)
