# Python code to demonstrate
# Common Row elements Summation
# using reduce() + lambda + set() + sum()

# initializing list of lists
from functools import reduce

test_list = [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]

# printing original list
print ("The original list is : " + str(test_list))

# Common Row elements Summation
# using reduce() + lambda + set() + sum()
res = sum(list(reduce(lambda i, j: i & j, (set(x) for x in test_list))))

# printing result
print ("The common row elements sum is : " + str(res))
