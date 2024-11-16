# importing pandas module
import pandas as pd

# importing regex module
import re

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org /wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace=True)

# returning top rows
new_data = data.head(10).copy()

# list for separate threshold values
threshold = [27, 23, 19, 30, 26, 22, 22, 41, 11, 33]

# applying method and returning to new column
new_data["Clipped values"] = new_data["Age"].clip_upper(threshold=threshold)

# display
new_data
