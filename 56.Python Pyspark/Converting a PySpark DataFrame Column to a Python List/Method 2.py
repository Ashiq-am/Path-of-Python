# convert student Name to list using map
print(dataframe.select('student Name').
	rdd.map(lambda x : x[0]).collect())

# convert student ID to list using map
print(dataframe.select('student ID').
	rdd.map(lambda x : x[0]).collect())

# convert student college to list using
# map
print(dataframe.select('college').
	rdd.map(lambda x : x[0]).collect())
