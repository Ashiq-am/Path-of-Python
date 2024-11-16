# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# removing null values
data.dropna(inplace = True)

# sorting in ascending order
data.sort_values("Salary", ascending = True, inplace = True)

# displaying top 5 values
data.head()
