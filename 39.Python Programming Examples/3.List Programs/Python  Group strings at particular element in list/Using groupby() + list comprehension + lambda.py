# Python3 code to demonstrate working of
# Group strings at particular element in list
# using groupby() + list comprehension + lambda
from itertools import groupby

# initialize lists
test_list = ['gfg', 'is', 'best', 'and', 'is', 'popular']

# printing original list
print("The original list is : " + str(test_list))

# initialize partition element
ele = 'is'

# Group strings at particular element in list
# using groupby() + list comprehension + lambda
res = [list(j) for i, j in groupby(test_list, lambda x:x == ele) if not i]

# printing result
print("Resultant list after grouping : " + str(res))
