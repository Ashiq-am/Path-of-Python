# Python3 code to demonstrate
# Flatten and Reverse Sort Matrix
# using itertools.chain() + sorted()
from itertools import chain

# initializing list of list
test_list = [[3, 5], [7, 3, 9], [1, 12]]

# printing original list of list
print("The original list : " + str(test_list))

# using itertools.chain() + sorted()
# Flatten and Reverse Sort Matrix
res = sorted(chain(*test_list), reverse = True)

# print result
print("The reverse sorted and flattened list : " + str(res))
