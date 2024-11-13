# Python3 code to demonstrate
# Sum of Uneven Lists of list
# Using chain() + sum()
from itertools import chain

# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))

# using chain() + sum()
# Sum of Uneven Lists of list
res = sum(list(chain(*test_list)))

# print result
print("The total element sum in lists is : " + str(res))
