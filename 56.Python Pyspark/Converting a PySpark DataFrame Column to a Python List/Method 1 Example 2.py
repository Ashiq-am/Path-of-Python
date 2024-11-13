# convert multiple columns to list using flatMap
print(dataframe.select(['student Name',
						'student Name',
						'college']).
	rdd.flatMap(lambda x: x).collect())
