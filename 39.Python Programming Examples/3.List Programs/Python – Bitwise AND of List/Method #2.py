# Python code to demonstrate working of
# Bitwise AND of List
# Using functools.reduce() + operator.iand
from operator import iand
from functools import reduce
# initializing list
test_list = [4, 6, 2, 3, 8, 9]

# printing original list
print("The original list is : " + str(test_list))

# Bitwise AND of List
# Using functools.reduce() + operator.iand
res = reduce(iand, test_list)

# printing result
print("The Bitwise AND of list elements are : " + str(res))
