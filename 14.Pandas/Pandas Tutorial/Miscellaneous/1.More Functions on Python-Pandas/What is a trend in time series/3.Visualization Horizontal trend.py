# importing the libraries
import pandas as pd
import matplotlib

# importing dataset
data = pd.read_csv(r'C:\Users\admin\Downloads\monthly-beer-production-in-austr.csv')

# casting Month column to datetime object
data['Month'] = pd.to_datetime(data['Month'])

# Setting Month as index
data = data.set_index('Month')

# Creating the plot
data['1984':'1994'].plot()
