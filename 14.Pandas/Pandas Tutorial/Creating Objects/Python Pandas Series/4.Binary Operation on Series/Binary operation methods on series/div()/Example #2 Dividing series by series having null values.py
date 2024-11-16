# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# passing age series to variable
age = data["Age"]

# na replacement
na = 200000

# Dividing values
# storing to new column
data["Divided values"]= data["Salary"].div(other = age, fill_value = na)

# display
data.head(10)
