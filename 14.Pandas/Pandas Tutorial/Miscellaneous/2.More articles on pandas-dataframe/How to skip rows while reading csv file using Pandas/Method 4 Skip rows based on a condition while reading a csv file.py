# Importing Pandas library
import pandas as pd

# function for checking and
# skipping every 3rd line
def logic(index):

	if index % 3 == 0:
		return True

	return False

# Skiping rows based on a condition
df = pd.read_csv("students.csv",
				skiprows = lambda x: logic(x) )

# Show the dataframe
df
