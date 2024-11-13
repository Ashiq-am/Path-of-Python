# Python code to find whether a sublist
# satisfies the triangle inequality.

# List initialization
Input = [[1, 1, 3], [4, 5, 6]]

# Sorting sublist of list of list
for elem in Input:
	elem.sort()

# Checking for triangular inequality
for elem in Input:
	if elem[0] + elem[1] > elem[2]:
		print(elem)
