# show dataframe by sorting the dataframe
# based on three columns in desc order
# using sort() function
dataframe.select(['student ID', 'student NAME', 'college']
				).sort(['student ID', 'student NAME', 'college'],
					ascending=False).show()
