# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace=True)

# start stop and step variables
start, stop, step = 0, -2, 2

# slicing till 2nd last element
data["Name"] = data["Name"].str.slice(start, stop, step)

# display
data.head(10)
