# Python code to demonstrate working of
# Bitwise OR among List elements
# Using reduce() + operator.ior
from operator import ior

# initializing list
test_list = [7, 8, 9, 1, 10, 7]

# printing original list
print("The original list is : " + str(test_list))

# Bitwise OR among List elements
# Using reduce() + operator.ior
res = reduce(ior, test_list)

# printing result
print("The Bitwise OR of list elements are : " + str(res))
