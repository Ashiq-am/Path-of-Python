# Python3 code to demonstrate working of
# Initial element index in Matrix
# Using accumulate() + map() + len()
from itertools import accumulate

# initializing list
test_list = [[5], [9, 3, 1, 4], [3, 2], [4, 7, 8, 3, 1, 2], [3, 4, 5]]

# printing original list
print("The original list is : " + str(test_list))

# ignoring last index using "-1"
# sum starting at 0
res = [0, *accumulate(map(len, test_list[:-1]))]

# printing result
print("Initial element indices : " + str(res))
