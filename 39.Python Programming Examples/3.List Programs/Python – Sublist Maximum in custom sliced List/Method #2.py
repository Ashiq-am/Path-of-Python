# Python3 code to demonstrate
# Sublist Maximum in custom sliced List
# using zip() + accumulate() + list slicing + max()
from itertools import accumulate

# initializing test list
test_list = [1, 5, 3, 7, 8, 10, 11, 16, 9, 12]

# initializing slice list
slice_list = [2, 1, 3, 4]

# printing original list
print("The original list : " + str(test_list))

# printing slice list
print("The slice list : " + str(slice_list))

# using zip() + accumulate() + list slicing + max()
# Sublist Maximum in custom sliced List
res = [max(test_list[i - j: i]) for i, j in zip(accumulate(slice_list), slice_list)]

# print result
print("The variable sliced list maximum is : " + str(res))
