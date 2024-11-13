# Python code to demonstrate
# Cube Summation in List
# using reduce() + lambda

# initializing list
from functools import reduce

test_list = [3, 5, 7, 9, 11]

# printing original list
print ("The original list is : " + str(test_list))

# using reduce() + lambda
# Cube Summation in List
res = reduce(lambda i, j: i + j * j*j, [test_list[:1][0]**3]+test_list[1:])

# printing result
print ("The sum of cubes of list is : " + str(res))
