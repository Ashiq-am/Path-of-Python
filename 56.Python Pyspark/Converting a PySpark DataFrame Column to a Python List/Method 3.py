# display college column in
# the list format using comphrension
print([data[0] for data in dataframe.
	select('college').collect()])


# display student ID column in the
# list format using comphrension
print([data[0] for data in dataframe.
	select('student ID').collect()])

# display subject1 column in the list
# format using comphrension
print([data[0] for data in dataframe.
	select('subject1').collect()])

# display subject2 column in the
# list format using comphrension
print([data[0] for data in dataframe.
	select('subject2').collect()])