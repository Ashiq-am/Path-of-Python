# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# removing null values
data.dropna(inplace = True)

# extracting least 5
least5 = data.nsmallest(5, "Salary")

# display
least5
