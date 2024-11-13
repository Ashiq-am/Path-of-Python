# Python code to sort a list of tuples
# according to given key.

# get the last key.
def last(n):
	return n[m]

# function to sort the tuple
def sort(tuples):

	# We pass used defined function last
	# as a parameter.
	return sorted(tuples, key = last)

# driver code
a = [(23, 45, 20), (25, 44, 39), (89, 40, 23)]
m = 2
print("Sorted:"),
print(sort(a))
