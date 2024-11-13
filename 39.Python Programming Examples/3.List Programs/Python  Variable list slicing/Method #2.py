# Python3 code to demonstrate
# variable length slicing
# using zip() + accumulate() + list slicing
from itertools import accumulate

# initializing test list
test_list = [1, 5, 3, 7, 8, 10, 11, 16, 9, 12]

# initializing slice list
slice_list = [2, 1, 3, 4]

# printing original list
print("The original list : " + str(test_list))

# printing slice list
print("The slice list : " + str(slice_list))

# using zip() + accumulate() + list slicing
# variable length slicing
res = [test_list[i - j: i] for i, j in zip(accumulate(slice_list), slice_list)]

# print result
print("The variable sliced list is : " + str(res))
