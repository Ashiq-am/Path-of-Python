# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# sorting by first name
data.sort_values("First Name", inplace = True)

# making a bool series
bool_series = data["First Name"].duplicated()

# displaying data
data.head()

# display data
data[bool_series]
