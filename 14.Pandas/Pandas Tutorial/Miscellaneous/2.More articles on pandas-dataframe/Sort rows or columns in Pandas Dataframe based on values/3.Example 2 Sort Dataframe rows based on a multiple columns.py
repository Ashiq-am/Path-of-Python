# import pandas library as pd
import pandas as pd

# List of Tuples
students = [('Ankit', 22, 'Up', 'Geu'),
		('Ananya', 31, 'Delhi', 'Gehu'),
		('Rahul', 16, 'Tokyo', 'Abes'),
		('Simran', 41, 'Delhi', 'Gehu'),
		('Shaurya', 33, 'Delhi', 'Geu'),
		('Harshita', 35, 'Mumbai', 'Bhu' ),
		('Priya', 35, 'Mp', 'Geu'),
		('Priya', 34, 'Uk', 'Geu'),
		('Jeet', 35, 'Guj', 'Gehu'),
		('Ananya', 35, 'Up', 'Bhu')
			]

# Create a DataFrame object from
# list of tuples with columns
# and indices.
details = pd.DataFrame(students, columns =['Name', 'Age',
										'Place', 'College'],
						index =[ 'b', 'c', 'a', 'e', 'f',
								'g', 'i', 'j', 'k', 'd'])

# sort Dataframe rows based on a 'Name' & 'Age' columns

# if duplicate value is present in 'Name' column
# then sorting will be done according to 'Age' column
rslt_df = details.sort_values(by = ['Name', 'Age'])

# show the resultant Dataframe
rslt_df
