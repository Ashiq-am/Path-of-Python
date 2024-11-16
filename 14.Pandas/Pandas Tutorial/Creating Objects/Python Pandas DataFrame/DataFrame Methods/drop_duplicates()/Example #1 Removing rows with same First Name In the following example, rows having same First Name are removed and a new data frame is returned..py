# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# sorting by first name
data.sort_values("First Name", inplace = True)

# dropping ALL duplicte values
data.drop_duplicates(subset ="First Name",
					keep = False, inplace = True)

# displaying data
data
