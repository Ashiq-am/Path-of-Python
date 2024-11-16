# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace=True)

# setting threshold value
threshold = 26.0

# applying method and passing to new column
data["Age_new"] = data["Age"].clip_lower(threshold)

# display
data
