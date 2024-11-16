# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# sorting by first name
data.sort_values("First Name", inplace = True)

# making a bool series
bool_series = data["First Name"].duplicated(keep = False)

# bool series
bool_series

# passing NOT of bool series to see unique values only
data = data[~bool_series]

# displaying data
data.info()
data
