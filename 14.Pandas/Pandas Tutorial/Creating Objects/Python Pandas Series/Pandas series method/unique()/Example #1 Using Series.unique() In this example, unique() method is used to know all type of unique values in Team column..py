# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# storing unique value in a variable
arr = data["Team"].unique()

# printing array
print(arr)
