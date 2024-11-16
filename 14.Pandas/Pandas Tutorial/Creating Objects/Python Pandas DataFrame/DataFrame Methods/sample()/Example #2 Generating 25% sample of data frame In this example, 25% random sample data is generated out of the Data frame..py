# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# generating one row
rows = data.sample(frac =.25)

# checking if sample is 0.25 times data or not

if (0.25*(len(data))== len(rows)):
	print( "Cool")
	print(len(data), len(rows))

# display
rows
