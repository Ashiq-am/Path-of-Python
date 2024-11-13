# show dataframe by sorting the dataframe
# based on two columns in asc
# order using orderBy() function
dataframe.select(['student NAME', 'college']
				).orderBy(['student NAME', 'college'],
						ascending=True).show()
