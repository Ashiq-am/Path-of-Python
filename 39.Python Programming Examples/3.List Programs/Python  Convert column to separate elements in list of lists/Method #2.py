# Python3 code to demonstrate
# column to separate elements in list of lists
# using itertools.chain()+ list comprehension + list slicing
from itertools import chain

# initializing list of list
test_list = [[1, 3, 4],
			[6, 2, 8],
			[9, 10, 5]]

# printing original list
print ("The original list is : " + str(test_list))

# using itertools.chain() + list comprehension + list slicing
# column to separate elements in list of lists
res = list(chain(*[list((sub[1: ], [sub[0]]))
					for sub in test_list]))

# printing result
print ("The list after colum shift is : " + str(res))
