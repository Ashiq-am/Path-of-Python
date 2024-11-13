# create tuples with college id
# and name and store in a list
data=[(1,'sravan'),(2,'ojaswi'),
	(3,'bobby'),(4,'rohith'),
	(5,'gnanesh')]

# map with lambda expression to get first element
first_data = map(lambda x: x[0], data)

# display data
for i in first_data:
	print(i)
