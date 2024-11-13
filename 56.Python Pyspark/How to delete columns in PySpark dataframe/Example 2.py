# delete two columns
dataframe=dataframe.drop(*('student NAME',
						'student ID'))
dataframe.show()
