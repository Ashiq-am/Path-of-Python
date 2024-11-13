# Python 3 code to demonstrate working of
# List Inversions
# Using map() + operator.invert
from operator import invert

# initializing list
test_list = [7, 8, 9, 1, 10, 7]

# printing original list
print("The original list is : " + str(test_list))

# List Inversions
# Using map() + operator.invert
res = list(map(invert, test_list))

# printing result
print("The Bitwise Inversions of list elements are : " + str(res))
