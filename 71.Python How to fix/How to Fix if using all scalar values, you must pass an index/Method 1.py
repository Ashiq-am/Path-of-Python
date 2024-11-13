# Importing pandas library
import pandas as pd

# Creating a dictionary or the data to
# be converted to the dataframe
dict = {'column-1': [1], 'column-2': [2],
		'column-3': [3], 'column-4': [4]}

# Converting to the dataframe
df = pd.DataFrame(dict)

print(df)
