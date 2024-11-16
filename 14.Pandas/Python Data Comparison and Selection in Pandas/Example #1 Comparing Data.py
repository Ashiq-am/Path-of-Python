# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# storing boolean series in new
new = data["Gender"] == "Male"

# inserting new series in data frame
data["New"]= new

# display
data
