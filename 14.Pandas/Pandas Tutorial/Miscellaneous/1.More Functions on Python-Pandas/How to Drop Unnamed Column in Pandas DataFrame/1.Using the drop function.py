# Import Pandas library
import pandas as pd

# Read the CSV file
df = pd.read_csv(
	'https://media.geeksforgeeks.org/wp-content/uploads/20240208164753/student_data3.csv')

# Print the data frame
print('Actual dataframe:')
print(df)

# Removing unnamed columns using drop function
df.drop(df.columns[df.columns.str.contains(
	'unnamed', case=False)], axis=1, inplace=True)

# Print the data frame after removing unnamed columns
print('\nDataframe after removing unnamed columns:')
print(df)
