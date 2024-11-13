# delete two columns
dataframe=dataframe.drop(*('student NAME',
						'student ID',
						'college'))
dataframe.show()
