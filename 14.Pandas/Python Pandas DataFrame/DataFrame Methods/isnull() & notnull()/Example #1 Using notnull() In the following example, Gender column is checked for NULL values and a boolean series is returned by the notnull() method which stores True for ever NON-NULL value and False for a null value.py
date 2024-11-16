# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# creating bool series False for NaN values
bool_series = pd.notnull(data["Gender"])

# displayed data only with team = NaN
data[bool_series]
