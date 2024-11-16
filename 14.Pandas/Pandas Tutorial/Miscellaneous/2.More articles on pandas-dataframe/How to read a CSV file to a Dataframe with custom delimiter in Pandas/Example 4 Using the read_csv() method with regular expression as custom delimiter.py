# Importing pandas library
import pandas as pd

# Load the data of example.csv
# with regular expression as
# custom delimiter into a
# Dataframe df
df = pd.read_csv('example4.csv',
				sep = '[:, |_]',
				engine = 'python')

# Print the Dataframe
df
