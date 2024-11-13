# convert student Name to list using
# flatMap
print(dataframe.select('student Name').
	rdd.flatMap(lambda x: x).collect())

# convert student ID to list using
# flatMap
print(dataframe.select('student ID').
	rdd.flatMap(lambda x: x).collect())
