# Count of students whose physics marks
# are greater than 10,chemistry marks are
# grater than 11 and math marks are greater than 9.
print("Count of students ->",
	dataframe[(dataframe['Physics'] > 10) &
				(dataframe['Chemistry'] > 11) &
				(dataframe['Math'] > 9)]['Name'].count())

# dataframe of above result
dataframe[(dataframe['Physics'] > 10 ) &
		(dataframe['Chemistry'] > 11 ) &
		(dataframe['Math'] > 9 )]
