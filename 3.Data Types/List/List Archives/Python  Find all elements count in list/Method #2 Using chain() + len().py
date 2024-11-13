# Python3 code to demonstrate
# count of all the elements in list
# Using chain() + len()
from itertools import chain

# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))

# using chain() + len()
# count of all the elements in list
res = len(list(chain(*test_list)))

# print result
print("The total element count in lists is : " + str(res))
