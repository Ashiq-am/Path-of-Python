# importing pandas module
import pandas as pd

# importing regex module
import re

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace=True)

# lower value of range
lower = 22

# upper value of range
upper = 25

# passing values to new column
data["New Age"] = data["Age"].clip(lower=lower, upper=upper)

# display
data
