# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# age series
age = data["Age"]

# na replacement
na = 5

# adding values
# storing to new column
data["Added values"]= data["Salary"].add(other = age, fill_value = na)

# display
data
