# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# making a bool series
bool_series = data["Salary"].between(80000, 100000, inclusive = True)

# returning dataframe with salary between above values
data[bool_series]
