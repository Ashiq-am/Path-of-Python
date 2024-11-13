# Python3 code to demonstrate working of
# Combine list with other list elements
# Using product()
from itertools import product

# initializing list
test_list = [3, 5, 7, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing pair list
pair_list = ['Gfg', 'is', 'best']

# product() performs pairing of elements
res = list(product([test_list], pair_list))

# printing result
print("The paired list : " + str(res))
