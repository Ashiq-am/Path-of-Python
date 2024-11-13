# Python code to find duplicate element in all
# sublist from list of list

# importing reduce
from functools import reduce

# function for set intersection
def func(a, b):
	return list(set(a).intersection(set(b)))

# List of list initialization
Input = [ [10, 20, 30, 40],
		[30, 40, 60, 70],
		[20, 30, 40, 60, 70],
		[30, 40, 80, 90], ]

# using reduce and set.intersection
out = reduce(func, Input)

# Printing output
print(out)
