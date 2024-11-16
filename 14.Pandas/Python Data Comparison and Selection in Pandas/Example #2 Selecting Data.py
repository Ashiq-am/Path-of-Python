# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# storing boolean series in new
new = data["Gender"] != "Female"

# inserting new series in data frame
data["New"]= new

# display
data[new]

# OR
# data[data["Gender"]=="Male"]
# Both are the same
