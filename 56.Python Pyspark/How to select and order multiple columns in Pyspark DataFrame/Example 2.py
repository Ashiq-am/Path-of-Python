# show dataframe by sorting the dataframe
# based on two columns in ascending
# order using sort() function
dataframe.select(['student ID', 'student NAME']
				).sort(['student ID', 'student NAME'],
					ascending=True).show()
