# Python3 code to demonstrate
# Valid Ranges Product
# Using itertools.groupby() + loop
from itertools import groupby


# getting Product
def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res


# initializing list
test_list = [4, 9, 0, 0, 3, 4, 5, 0, 0, 4, 0]

# printing original list
print("The original list : " + str(test_list))

# using itertools.groupby() + loop
# Valid Ranges Product
res = [prod(val) for keys, val in groupby(test_list, key=lambda x: x != 0) if keys != 0]

# print result
print("The non-zero group product of list is : " + str(res))
