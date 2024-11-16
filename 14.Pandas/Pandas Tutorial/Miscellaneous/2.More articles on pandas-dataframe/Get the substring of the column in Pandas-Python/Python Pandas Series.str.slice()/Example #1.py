# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace=True)

# start stop and step variables
start, stop, step = 0, -2, 1

# converting to string data type
data["Salary"] = data["Salary"].astype(str)

# slicing till 2nd last element
data["Salary (int)"] = data["Salary"].str.slice(start, stop, step)

# display
data.head(10)
