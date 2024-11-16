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
						index =['a', 'b', 'c', 'd', 'e',
								'f', 'g', 'i', 'j', 'k'])

# Get a bool series representing which row
# satisfies the condition i.e. True for
# row in which 'College' is 'Geu'
details = details.apply(lambda x : True
			if x['College'] == "Geu" else False, axis = 1)

# Count number of True in the series
num_rows = len(details[details == True].index)

print('Number of Rows in dataframe in which College is Geu : ',
	num_rows )
