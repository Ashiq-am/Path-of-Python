# Importing the library
import pandas as pd

# Creating the data frame
details = {
	'col1': [1, 3, 5, 7, 9],
	'col2': [7, 4, 35, 14, 56]
}

# creating a Dataframe object
df = pd.DataFrame(details)

# Z-Score using pandas
df['col1'] = (df['col1'] - df['col1'].mean()) / df['col1'].std()
