# delete two columns
dataframe = dataframe.drop(*('Employee NAME',
							'Employee ID'))
dataframe.show()
