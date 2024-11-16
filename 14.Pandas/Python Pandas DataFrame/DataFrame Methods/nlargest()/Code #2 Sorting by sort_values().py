# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# removing null values
data.dropna(inplace = True)

# sorting in descending order
data.sort_values("Salary", ascending = False, inplace = True)

# displaying top 5 values
data.head()
