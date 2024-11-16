# importing the libraries
import pandas as pd
import matplotlib

# importing dataset
data = pd.read_csv(r'C:\Users\admin\Downloads\Electric_Production.csv')

# casting Month column to datetime object
data['DATE'] = pd.to_datetime(data['DATE'])

# Setting Month as index
data = data.set_index('DATE')

# Creating the plot
data.plot()
