# display college column in
# the list format using toPandas
print(list(dataframe.select('college').
		toPandas()['college']))


# display student NAME column in
# the list format using toPandas
print(list(dataframe.select('student NAME').
		toPandas()['student NAME']))

# display subject1 column in
# the list format using toPandas
print(list(dataframe.select('subject1').
		toPandas()['subject1']))

# display subject2 column
# in the list format using toPandas
print(list(dataframe.select('subject2').
		toPandas()['subject2']))
