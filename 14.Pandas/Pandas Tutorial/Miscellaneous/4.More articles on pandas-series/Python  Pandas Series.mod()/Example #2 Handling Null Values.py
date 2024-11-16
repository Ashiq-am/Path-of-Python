# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# creating short data of 5 rows
short_data = data.head()

# creating list with 5 values
list = [1, 2, 3, 4, 3]

# replacing null value with any number
null_replacement = 21218

# finding remainder
# creating new column
short_data["Remainder"] = short_data["Salary"].mod(list, fill_value=null_replacement)

# display
short_data
