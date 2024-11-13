# Python code to sort the tuples using float element
# Inplace way to sort using sort()
def Sort(tup):
	# reverse = True (Sorts in Descending order)
	# key is set to sort using float elements
	# lambda has been used
	tup.sort(key = lambda x: float(x[1]), reverse = True)
	print(tup)

# Driver Code
tup = [('lucky', '18.265'), ('nikhil', '14.107'), ('akash', '24.541'),
	('anand', '4.256'), ('gaurav', '10.365')]
Sort(tup)
