# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dividing age series
data["Age"]= data["Age"]/100

age = data["Age"]

# na replacement
na = 20

# Multiplying values
# storing to new column
data["Multiplied values"]= data["Salary"].mul(other = age, fill_value = na)

# display
data
