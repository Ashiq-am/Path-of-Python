# importing pandas library
import pandas as pd

# Creating a Data frame
df = pd.DataFrame([['Date1', 1850, 1992,'Avi', 5, 41, 70, 'Avi'],
				['Date2', 1896, 1950, 'Cathy', 10, 1, 22, 'Avi'],
				['Date2', 1900, 1920, 'Cathy', 24, 11, 44, 'Cathy'],
				['Date1', 1889, 1960, 'Bob', 2, 11, 10, 'Bob'],
				['Date2', 1910, 1952, 'Avi', 20, 10, 40, 'Bob'],
				['Date1', 1999, 1929, 'Avi', 50, 8, 11, 'Cathy']],
				columns=('Year', 'Date1', 'Date2', 'Name', 'Avi',
						'Bob', 'Cathy', 'Alpha'))

# Display Data frame
df
