# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# removing null values
data.dropna(inplace = True)

# extracting greatest 5
large5 = data.nlargest(5, "Salary")

# display
large5
