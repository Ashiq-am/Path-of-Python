# find average of multiple column
dataframe.agg({'subject 1': 'avg',
			'student ID': 'avg',
			'subject 2': 'avg'}).show()
