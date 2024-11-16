# Import the pandas library
import pandas as pd

# Define the data
data = {'first_name': ['Arun', 'Ishita', 'Ruchir', 'Vinayak'], 'last_name': [
	'Kumar', 'Rai', 'Jha', 'Rai'], 'fees': [5000, 6000, 5000, 6000]}

# Convert data to Pandas dataframe
df = pd.DataFrame(data)

# Print the actual data frame
print('Actual DataFrame:\n', df)

# Stating the column that you want to ignore
dropped_df = df.drop_duplicates(subset=df.columns.difference(['first_name']))

# Print the dataframe without duplicates
print('DataFrame after removing duplicates:\n', dropped_df)
