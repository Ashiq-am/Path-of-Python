# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv")

# sorting data frame by name
data.sort_values("Salary", axis = 0, ascending = True,
				inplace = True, na_position ='first')

data
# display
