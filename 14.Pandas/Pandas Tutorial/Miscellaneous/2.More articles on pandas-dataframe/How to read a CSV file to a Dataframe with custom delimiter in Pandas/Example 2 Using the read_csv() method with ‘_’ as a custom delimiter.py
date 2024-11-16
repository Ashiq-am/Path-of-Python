# Importing pandas library
import pandas as pd

# Load the data of example.csv
# with '_' as custom delimiter
# into a Dataframe df
df = pd.read_csv('example2.csv',
				sep = '_',
				engine = 'python')

# Print the Dataframe
df
