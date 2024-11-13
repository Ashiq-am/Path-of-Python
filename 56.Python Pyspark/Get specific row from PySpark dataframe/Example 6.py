# select first row
print(dataframe.select(['Employee ID',
						'Employee NAME',
						'Company Name']).collect()[0])

# select third row
print(dataframe.select(['Employee ID',
						'Employee NAME',
						'Company Name']).collect()[2])

# select forth row
print(dataframe.select(['Employee ID',
						'Employee NAME',
						'Company Name']).collect()[3])
