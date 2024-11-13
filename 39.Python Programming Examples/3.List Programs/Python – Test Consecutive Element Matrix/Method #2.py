# Python3 code to demonstrate working of
# Test Consecutive Element Matrix
# Using chain.from_iterable() + all()
from itertools import chain

# initializing list
test_list = [[4, 5, 6], [7], [8, 9, 10], [11, 12]]

# printing original list
print("The original list is : " + str(test_list))

# flattening matrix
test_list = list(chain.from_iterable(test_list))

# checking for boolean true
res = all(test_list[idx - 1] == test_list[idx] -
		1 for idx in range(1, len(test_list)))

# printing result
print("Is Matrix Consecutive ? : " + str(res))
