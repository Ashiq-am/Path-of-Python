# Python3 code to demonstrate
# summation of non-zero groups
# Using itertools.groupby() + sum()
from itertools import groupby

# initializing list
test_list = [4, 9, 0, 0, 3, 4, 5, 0, 0, 4, 0]

# printing original list
print("The original list : " + str(test_list))

# using itertools.groupby() + sum()
# summation of non-zero groups
res = [sum(val) for keys, val in groupby(test_list,
			key = lambda x: x != 0) if keys != 0]

# print result
print("The non-zero group summation of list is : " + str(res))
