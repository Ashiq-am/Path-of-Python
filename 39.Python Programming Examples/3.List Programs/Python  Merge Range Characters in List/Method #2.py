# Python code to demonstrate
# Merge Range Characters in List
# using reduce() + lambda + list slicing

# initializing list
from functools import reduce

test_list = ['I', 'L', 'O', 'V', 'E', 'G', 'F', 'G']

# printing original list
print ("The original list is : " + str(test_list))

# initializing strt, end
strt, end = 3, 7

# using reduce() + lambda + list slicing
# Merge Range Characters in List
test_list[strt : end] = [reduce(lambda i, j: i + j, test_list[strt : end])]

# printing result
print ("The list after merging elements : " + str(test_list))
