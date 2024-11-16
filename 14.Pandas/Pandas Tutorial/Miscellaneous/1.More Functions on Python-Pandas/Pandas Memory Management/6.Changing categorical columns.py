# importing the modules
import pandas
import numpy

# Reading the csv file
df = pd.read_csv('data.csv')

# Memory usage before replacing
df['bedrooms'].memory_usage()
# output--> 314640

# Replacing the categorical values
df['bedrooms'].replace('more than 2', 1, inplace=True)
df['bedrooms'].replace('less than 2', 0, inplace=True)

# Memory usage after replacing
df['bedrooms'].memory_usage()
# output--> 173032
