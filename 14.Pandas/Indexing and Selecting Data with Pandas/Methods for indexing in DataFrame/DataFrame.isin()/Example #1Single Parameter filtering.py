'''
In the following Example, Rows are checked and a boolean series is
returned which is True wherever Gender=”Male”. Then the series is passed
to data frame to see new filtered data frame.


'''



# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# creating a bool series from isin()
new = data["Gender"].isin(["Male"])

# displaying data with gender = male only
data[new]
