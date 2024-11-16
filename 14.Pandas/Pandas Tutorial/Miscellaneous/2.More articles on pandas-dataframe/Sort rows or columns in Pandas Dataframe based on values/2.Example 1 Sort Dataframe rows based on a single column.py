# import pandas library as pd
import pandas as pd

# List of Tuples
students = [('Ankit', 22, 'Up', 'Geu'),
		('Ankita', 31, 'Delhi', 'Gehu'),
		('Rahul', 16, 'Tokyo', 'Abes'),
		('Simran', 41, 'Delhi', 'Gehu'),
		('Shaurya', 33, 'Delhi', 'Geu'),
		('Harshita', 35, 'Mumbai', 'Bhu' ),
		('Swapnil', 35, 'Mp', 'Geu'),
		('Priya', 35, 'Uk', 'Geu'),
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

# Sort the rows of dataframe by 'Name' column
rslt_df = details.sort_values(by = 'Name')

# show the resultant Dataframe
rslt_df
