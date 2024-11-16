"""
In the following example, the data frame is filtered on the basis
of Gender as well as Team. Rows having Gender=”Female” and
Team=”Engineering”, “Distribution” or “Finance” are returned

"""


# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# creating filters of bool series from isin()
filter1 = data["Gender"].isin(["Female"])
filter2 = data["Team"].isin(["Engineering", "Distribution", "Finance" ])

# displaying data with both filter applied and mandatory
data[filter1 & filter2]
