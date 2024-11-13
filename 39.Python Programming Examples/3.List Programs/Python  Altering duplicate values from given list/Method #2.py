# Python3 code to demonstrate
# Altering duplicated
# using itertools.groupby() + list comprehension
from itertools import groupby

# initializing list
test_list = [2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]

# printing original list
print("The original list : " + str(test_list))

# using itertools.groupby() + list comprehension
# Altering duplicated
res = [val for key, grp in groupby(test_list)
	for val in [key] + [False] * (len(list(grp))-1)]

# print result
print("The altered duplicate list is : " + str(res))
