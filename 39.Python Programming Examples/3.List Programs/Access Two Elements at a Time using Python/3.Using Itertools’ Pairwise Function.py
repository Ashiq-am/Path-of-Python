from itertools import tee

# initializing Lists
data = [1, 2, 3, 4]

# Defining a function to create pairwise iterable
def pairwise(iterable):
	a, b = tee(iterable)
	next(b, None)
	return zip(a, b)

# Accessing two elements at a time using the pairwise function
for elem1, elem2 in pairwise(data):
	print(elem1, elem2)
