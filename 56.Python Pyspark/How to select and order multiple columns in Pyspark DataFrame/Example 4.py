# show dataframe by sorting the dataframe
# based on three columns in desc
# order using orderBy() function
dataframe.select(['student ID', 'student NAME', 'college']
				).orderBy(['student ID', 'student NAME', 'college'],
						ascending=False).show()
