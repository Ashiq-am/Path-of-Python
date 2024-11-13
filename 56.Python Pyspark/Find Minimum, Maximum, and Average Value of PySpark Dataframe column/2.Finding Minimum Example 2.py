# minimum value from multiple column
dataframe.agg({'college': 'min',
			'student NAME': 'min',
			'student ID':'min'}).show()
