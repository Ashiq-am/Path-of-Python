# Python code to merge elements of sublists

from operator import concat
from itertools import starmap

# Initialisation of first list
list1 = [[1, 20, 30],
		[40, 29, 72],
		[119, 123, 115]]

# Initialisation of second list
list2 = [[29, 57, 64, 22],
		[33, 66, 88, 15],
		[121, 100, 15, 117]]

# Using starmap() and concat to merge list
Output = list(starmap(concat, zip(list1, list2)))

# Printing output
print(Output)
