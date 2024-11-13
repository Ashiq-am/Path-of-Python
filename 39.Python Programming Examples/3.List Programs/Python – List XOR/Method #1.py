# Python code to demonstrate working of
# List XOR
# Using reduce() + lambda + "^" operator

# initializing list
from functools import reduce

test_list = [4, 6, 2, 3, 8, 9]

# printing original list
print("The original list is : " + str(test_list))

# List XOR
# Using reduce() + lambda + "^" operator
res = reduce(lambda x, y: x ^ y, test_list)

# printing result
print("The Bitwise XOR of list elements are : " + str(res))
