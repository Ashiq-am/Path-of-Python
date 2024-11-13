# Python code to demonstrate working of
# Bitwise OR among List elements
# Using reduce() + lambda + "|" operator

# initializing list
from functools import reduce

test_list = [7, 8, 9, 1, 10, 7]

# printing original list
print("The original list is : " + str(test_list))

# Bitwise OR among List elements
# Using reduce() + lambda + "|" operator
res = reduce(lambda x, y: x | y, test_list)

# printing result
print("The Bitwise OR of list elements are : " + str(res))
