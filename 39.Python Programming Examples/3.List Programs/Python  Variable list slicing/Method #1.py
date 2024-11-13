# Python3 code to demonstrate
# variable length slicing
# using itertools.islice() + list comprehension
from itertools import islice

# initializing test list
test_list = [1, 5, 3, 7, 8, 10, 11, 16, 9, 12]

# initializing slice list
slice_list = [2, 1, 3, 4]

# printing original list
print("The original list : " + str(test_list))

# printing slice list
print("The slice list : " + str(slice_list))

# using itertools.islice() + list comprehension
# variable length slicing
temp = iter(test_list)
res = [list(islice(temp, part)) for part in slice_list]

# print result
print("The variable sliced list is : " + str(res))
