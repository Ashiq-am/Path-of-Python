# Import the pandas library
import pandas as pd

# Define the data
data = {'first_name': ['Arun', 'Ishita', 'Ruchir', 'Vinayak'], 'last_name': [
	'Kumar', 'Rai', 'Jha', 'Rai'], 'fees': [5000, 6000, 5000, 6000]}

# Convert data to Pandas dataframe
df = pd.DataFrame(data)

# Print the actual data frame
print('Actual DataFrame:\n', df)

# Defining the list of columns that you want to consider
dropped_df = df.drop_duplicates(subset=['last_name', 'fees'])

# Print the dataframe without duplicates
print('DataFrame after removing duplicates:\n', dropped_df)
