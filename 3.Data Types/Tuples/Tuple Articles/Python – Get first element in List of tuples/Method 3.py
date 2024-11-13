import operator

# create tuples with college id
# and name and store in a list
data = [(1,'sravan'),(2,'ojaswi'),
		(3,'bobby'),(4,'rohith'),
		(5,'gnanesh')]

# map the data using item
# getter method with first elements
first_data = map(operator.itemgetter(0), data)

# display first elements
for i in first_data:
	print(i)
