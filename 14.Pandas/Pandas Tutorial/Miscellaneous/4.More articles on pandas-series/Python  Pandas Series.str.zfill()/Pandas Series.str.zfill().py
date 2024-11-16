# importing pandas
import pandas as pd

# making data frame from csv at url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/employees.csv")

# converting to string dtype
data["Salary"] = data["Salary"].astype(str)

# width of output string
width = 10

# calling method and overwriting series
data["Salary"] = data["Salary"].str.zfill(width)

# display
data
