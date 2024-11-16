''''''
"""Two data frames are made. A column with all values = none is added to the new Data frame. 
Column names are verified to see if the Null column was inserted properly. Then Number of columns is 
compared before and after dropping NaN values."""


# importing pandas module
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv")

# making a copy of old data frame
new = pd.read_csv("nba.csv")

# creating a value with all null values in new data frame
new["Null Column"]= None

# checking if column is inserted properly
print(data.columns.values, "\n", new.columns.values)

# comparing values before dropping null column
print("\nColumn number before dropping Null column\n",
	len(data.dtypes), len(new.dtypes))

# dropping column with all null values
new.dropna(axis = 1, how ='all', inplace = True)

# comparing values after dropping null column
print("\nColumn number after dropping Null column\n",
	len(data.dtypes), len(new.dtypes))
