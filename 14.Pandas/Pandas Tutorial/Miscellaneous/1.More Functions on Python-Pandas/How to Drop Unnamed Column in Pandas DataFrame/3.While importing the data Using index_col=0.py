# Import Pandas library
import pandas as pd

# create DataFrame
df1 = pd.DataFrame({'name': ['Arun', 'Aniket', 'Ishits', 'Pranjal', 'Vinayak'],
					'subject': ['Maths', 'Social Science', 'English', 'Science', 'Computer'],
					'fees': [9000, 12000, 15000, 18000, 18000]})

# Store the data frame in a CSV file
df1.to_csv('student_data.csv')

# Read the CSV file
df = pd.read_csv('student_data.csv')

# Print the data frame
print('Actual dataframe:')
print(df)

# Read the CSV file removing unnamed columns
df = pd.read_csv('student_data.csv', index_col=0)

# Print the data frame after removing unnamed columns
print('\nDataframe after removing unnamed columns:')
print(df)
