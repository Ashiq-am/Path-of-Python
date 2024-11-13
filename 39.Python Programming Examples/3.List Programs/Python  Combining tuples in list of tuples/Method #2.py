# Python3 code to demonstrate
# Combining tuples in list of tuples
# Using product() + list comprehension
from itertools import product

# initializing list
test_list = [([1, 2, 3], 'gfg'), ([5, 4, 3], 'cs')]

# printing original list
print("The original list : " + str(test_list))

# Using product() + list comprehension
# Combining tuples in list of tuples
res = [ele for i, j in test_list for ele in product(i, [j])]

# print result
print("The list tuple combination : " + str(res))
