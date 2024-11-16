# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# creating short data of 5 rows
short_data = data.head()

# creating list with 5 values
list =[5, 4, 3, 2, 1]

# subtracting list data
# creating new column
short_data["Subtracted values"]= short_data["Salary"].sub(list)

# display
short_data
