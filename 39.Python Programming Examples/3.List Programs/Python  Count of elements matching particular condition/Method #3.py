# Python 3 code to demonstrate
# to get count of elements matching condition
# using reduce() + lambda

# initializing list
from functools import reduce

test_list = [3, 5, 1, 6, 7, 9]

# printing original list
print ("The original list is : " + str(test_list))

# using reduce() + lambda
# to get count of elements matching condition
# checks for odd
res = reduce(lambda count, i: count + (i % 2 != 0), test_list, 0)

# printing result
print ("The number of odd elements: " + str(res))
