# Python3 code to demonstrate working of
# Minimum identical consecutive Subarray
# using groupby() + min() + lambda
from itertools import groupby

# initializing list
test_list = [1, 1, 1, 2, 2, 5, 5, 5, 5]

# printing original list
print("The original list is : " + str(test_list))

# Minimum identical consecutive Subarray
# using groupby() + min() + lambda
temp = groupby(test_list)
res = min(temp, key = lambda sub: len(list(sub[1])))

# printing result
print("Minimum Consecutive identical Occurring number is : " + str(res[0]))
