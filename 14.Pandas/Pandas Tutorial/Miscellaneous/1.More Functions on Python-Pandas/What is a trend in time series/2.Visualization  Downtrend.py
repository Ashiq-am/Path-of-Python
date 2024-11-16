import pandas as pd
import matplotlib

# importing dataset
data = pd.read_csv(r'C:\Users\admin\Downloads\AlcoholSale.csv')

# casting Date column to datetime object
data['DATE'] = pd.to_datetime(data['DATE'])

# Setting Date column as index
data = data.set_index('DATE')

# Creating the plot
data.plot()
