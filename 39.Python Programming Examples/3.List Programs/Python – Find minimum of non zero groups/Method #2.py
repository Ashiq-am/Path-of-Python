# Python3 code to demonstrate
# Natural Numbers Minimum
# Using itertools.groupby() + min()
from itertools import groupby

# initializing list
test_list = [4, 9, 0, 0, 3, 4, 5, 0, 0, 4, 0]

# printing original list
print("The original list : " + str(test_list))

# using itertools.groupby() + min()
# Natural Numbers Minimum
res = [min(val) for keys, val in groupby(test_list, key = lambda x: x != 0) if keys != 0]

# print result
print("The non-zero group minimum of list is : " + str(res))
