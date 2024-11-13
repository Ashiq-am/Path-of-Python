# maximum value from multiple column
dataframe.agg({'college': 'max',
			'student NAME': 'max',
			'student ID':'max'}).show()
