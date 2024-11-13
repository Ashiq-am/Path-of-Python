# Python code to demonstrate
# i ^ k Summation in list
# using reduce() + lambda + pow()

# initializing list
from functools import reduce

test_list = [3, 5, 7, 9, 11]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 4

# using reduce() + lambda + pow()
# i ^ k Summation in list
res = reduce(lambda i, j: i + pow(j, K), [pow(test_list[:1][0], K)] + test_list[1:])

# printing result
print ("The sum of i ^ k of list is : " + str(res))
