# import pandas library as pd
import pandas as pd

# List of Tuples
students = [
		(75, 50, 60, 70),
		(75, 55, 65, 75),
		(75, 35, 45, 25),
		(75, 90, 60, 70),
		(76, 90, 70, 60),
		(90, 80, 70, 60),
		(65, 10, 30, 20)
			]

# Create a DataFrame object from
# list of tuples with columns
# and indices.
details = pd.DataFrame(students, columns =['Hindi', 'Math',
										'Science', 'English'],
						index = ['Ankit', 'Rahul', 'Aishwarya',
								'Shivangi', 'Priya', 'Swapnil',
								'Shaurya'])

# sort Dataframe columns based on a 'Shivangi' & 'Priya' rows

# if duplicate value is present in 'Shivangi' row
# then sorting will be done according to 'Priya' row
rslt_df = details.sort_values(by = ['Shivangi', 'Priya'], axis = 1)

rslt_df
