# import module
import pandas as pd

# read CSV file
results = pd.read_csv('Data.csv')

# count no. of lines
print("Number of lines present:-",
	len(results))
