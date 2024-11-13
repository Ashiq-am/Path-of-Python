# Python3 code to demonstrate
# smallest number greater than K
# using sort() + bisect_right()
from bisect import bisect_right

# Initializing list
test_list = [1, 4, 7, 5, 10]

# Initializing k
k = 6

# Printing original list
print ("The original list is : " + str(test_list))

# Using sort() + bisect_right()
# to find smallest number
# greater than K
test_list.sort()
min_val = test_list[bisect_right(test_list, k)]

# Printing result
print ("The minimum value greater than 6 is : " + str(min_val))
