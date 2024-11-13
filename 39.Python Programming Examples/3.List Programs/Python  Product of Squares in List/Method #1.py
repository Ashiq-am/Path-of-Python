# Python code to demonstrate
# Product of Squares in List
# using reduce() + lambda

# initializing list
from functools import reduce

test_list = [3, 5, 7, 9, 11]

# printing original list
print ("The original list is : " + str(test_list))

# using reduce() + lambda
# Product of Squares in List
res = reduce(lambda i, j: i * j*j, [test_list[:1][0]**2]+test_list[1:])

# printing result
print ("The product of squares of list is : " + str(res))
