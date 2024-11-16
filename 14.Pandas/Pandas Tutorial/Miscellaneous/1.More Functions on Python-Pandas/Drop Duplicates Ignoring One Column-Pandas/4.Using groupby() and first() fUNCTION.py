# Import the pandas library
import pandas as pd

# Define the data
data = {'first_name': ['Arun', 'Ishita', 'Ruchir', 'Vinayak'], 'last_name': [
	'Kumar', 'Rai', 'Jha', 'Rai'], 'fees': [5000, 6000, 5000, 6000]}

# Convert data to Pandas dataframe
df = pd.DataFrame(data)

# Print the actual data frame
print('Actual DataFrame:\n', df)

# Dropping the duplicates using groupby and first
dropped_df = df.groupby(['last_name', 'fees']).first()

# Print the dataframe without duplicates
print('DataFrame after removing duplicates:\n', dropped_df)
