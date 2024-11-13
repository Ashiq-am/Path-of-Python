# group by studentID by marks
dataframe = dataframe.groupBy(
'student ID').sum('subject marks')

# display count of unique ID
print("Unique ID count after Group By : ",
	dataframe.distinct().count())

print("the data is ")

# display values of unique ID
dataframe.distinct().show()
