# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# age series
age = data["Age"]

# na replacement
na = 20

# adding values
# storing to new column
data["Subtracted values"]= data["Salary"].sub(other = age, fill_value = na)

# display
data
