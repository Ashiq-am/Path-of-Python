# Python3 code to demonstrate working of
# Union multiple sets
# Using chain.from_iterable() + * operator
from itertools import chain

# initializing list
test_list = [{4, 3, 5, 2}, {8, 4, 7, 2}, {1, 2, 3, 4}, {9, 5, 3, 7}]

# printing original list
print("The original list is : " + str(test_list))

# * operator packs sets for union
res = set(chain(*test_list))

# printing result
print("Multiple set union : " + str(res))
