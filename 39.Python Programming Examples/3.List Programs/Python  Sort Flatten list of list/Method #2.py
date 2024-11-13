# Python3 code to demonstrate
# sort flatten list of list
# using itertools.chain() + sorted()
from itertools import chain

# initializing list of list
test_list = [[3, 5], [7, 3, 9], [1, 12]]

# printing original list of list
print("The original list : " + str(test_list))

# using itertools.chain() + sorted()
# sort flatten list of list
res = sorted(chain(*test_list))

# print result
print("The sorted and flattened list : " + str(res))
