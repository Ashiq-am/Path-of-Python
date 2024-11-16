# importing libraries
import pandas as pd

# Storing data in dictionary
details = {
	'Column1': [1, 2, 3, 4],
	'Column2': [7, 4, 25, 9],
	'Column3': [3, 8, 10, 30],
	'Column4': [7, 4, 25, 9],
}

# creating a Dataframe object
df = pd.DataFrame(details)

df['Column4'].equals(df['Column2']) # Returns True

# df['Column1'].equals(df['Column2']) Returns False
