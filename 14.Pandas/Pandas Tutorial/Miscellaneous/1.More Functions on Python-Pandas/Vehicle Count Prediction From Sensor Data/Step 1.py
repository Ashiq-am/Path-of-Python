# importing the pandas module for
# data frame
import pandas as pd


# load the data set into train variable.
train = pd.read_csv('vehicles.csv')

# display top 5 values of data set
train.head()
