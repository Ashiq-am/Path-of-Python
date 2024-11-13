# Python code to demonstrate
# merging list elements
# using reduce() + lambda + list slicing

# initializing list
from functools import reduce

test_list = ['I', 'L', 'O', 'V', 'E', 'G', 'F', 'G']

# printing original list
print ("The original list is : " + str(test_list))

# using reduce() + lambda + list slicing
# merging list elements
test_list[5 : 8] = [reduce(lambda i, j: i + j, test_list[5 : 8])]

# printing result
print ("The list after merging elements : " + str(test_list))
