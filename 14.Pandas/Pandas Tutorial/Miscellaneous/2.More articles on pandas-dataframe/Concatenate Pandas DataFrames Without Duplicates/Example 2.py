# Importing pandas library
import pandas as pd

# loading dataframes
dataframe1 = pd.DataFrame({'name': ['rahul', 'anjali', 'kajal'],
						'age': [23, 28, 30]})

dataframe2 = pd.DataFrame({'name': ['devesh', 'rashi', 'anjali'],
						'age': [20, 15, 28]})

# Concatenating two dataframes wtithout duplicates
new_dataframe = pd.concat([dataframe1, dataframe2]).drop_duplicates()

# Resetting index
new_dataframe = new_dataframe.reset_index(drop=True)

# Display dataframe generated
new_dataframe
