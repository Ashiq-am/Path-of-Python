# Importing pandas module
import pandas as pd

# Creating a dictionary
dit = {'August': [10, 25, 34, 4.85, 71.2, 1.1],
	'September': [4.8, 54, 68, 9.25, 58, 0.9],
	'October': [78, 5.8, 8.52, 12, 1.6, 11],
	'November': [100, 5.8, 50, 8.9, 77, 10]}

# Converting it to data frame
df = pd.DataFrame(data=dit)

# Original DataFrame
df
