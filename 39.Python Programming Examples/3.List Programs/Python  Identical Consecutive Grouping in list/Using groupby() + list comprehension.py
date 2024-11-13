# Python3 code to demonstrate working of
# Identical Consecutive Grouping in list
# using groupby() + list comprehension
from itertools import groupby

# initialize list
test_list = [4, 4, 5, 5, 5, 7, 7, 8, 8, 8]

# printing original list
print("The original list is : " + str(test_list))

# Identical Consecutive Grouping in list
# using groupby() + list comprehension
res = [list(y) for x, y in groupby(test_list)]

# printing result
print("List after grouping is : " + str(res))
