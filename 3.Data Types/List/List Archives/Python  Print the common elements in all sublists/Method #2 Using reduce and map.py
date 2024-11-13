# Python code to find duplicate element in all
# sublist from list of list
import operator
from functools import reduce

# List of list initialization
Input = [ [10, 20, 30, 40],
		[30, 40, 60, 70],
		[20, 30, 40, 60, 70],
		[30, 40, 80, 90], ]

# using reduce and map
out = reduce(operator.iand, map(set, Input))

# Converting into list
out = list(out)

# Printing output
print(out)
