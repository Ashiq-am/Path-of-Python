'''
'''
'''Data frame is read and all rows with any Null values are dropped. The size of old and new data frames 
is compared to see how many rows had at least 1 Null value.'''


# importing pandas module
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv")

# making new data frame with dropped NA values
new_data = data.dropna(axis = 0, how ='any')

# comparing sizes of data frames
print("Old data frame length:", len(data), "\nNew data frame length:",
	len(new_data), "\nNumber of rows with at least 1 NA value: ",
	(len(data)-len(new_data)))
