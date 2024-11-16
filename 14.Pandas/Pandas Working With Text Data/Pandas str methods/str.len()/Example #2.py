''''''
'''In this example, the length of salary column is calculated using the str.len() method. 
Since the series is imported as float64 dtype, it’s first converted to string using .astype() method.'''

# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace = True)

# converting to string dtype
data["Salary"]= data["Salary"].astype(str)

# passing values
data["Salary Length"]= data["Salary"].str.len()

# converting back to float dtype
data["Salary"]= data["Salary"].astype(float)

# display
data
