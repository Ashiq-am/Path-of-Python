# Python code to remove all strings from a list of tuples

# Creating list of tuples
listOfTuples = [('string', 'Geeks'), (2, 225), (3, '111'),
								(4, 'Cyware'), (5, 'Noida')]


output = [tuple(j for j in i if not isinstance(j, str))
								for i in listOfTuples]

# printing output
print(output)
