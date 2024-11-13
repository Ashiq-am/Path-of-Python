# Python code to demonstrate
# Cubes Product in list
# using reduce() + lambda

# initializing list
from functools import reduce

test_list = [3, 5, 7, 9, 11]

# printing original list
print ("The original list is : " + str(test_list))

# using reduce() + lambda
# Cubes Product in list
res = reduce(lambda i, j: i * j*j * j, [test_list[:1][0]**3]+test_list[1:])

# printing result
print ("The product of cubes of list is : " + str(res))
