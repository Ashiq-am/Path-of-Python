# Python code to sort the tuples using float element
# Function to sort using sorted()
def Sort(tup):
	# reverse = True (Sorts in Descending order)
	# key is set to sort using float elements
	# lambda has been used
	return(sorted(tup, key = lambda x: float(x[1]), reverse = True))

# Driver Code
tup = [('lucky', '18.265'), ('nikhil', '14.107'), ('akash', '24.541'),
	('anand', '4.256'), ('gaurav', '10.365')]
print(Sort(tup))
