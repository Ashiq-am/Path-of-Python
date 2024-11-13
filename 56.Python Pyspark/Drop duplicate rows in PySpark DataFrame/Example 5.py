# remove duplicate data using
# dropDuplicates() function in
# two columns
dataframe.select(['Employee ID', 'Employee NAME']
				).dropDuplicates().show()
