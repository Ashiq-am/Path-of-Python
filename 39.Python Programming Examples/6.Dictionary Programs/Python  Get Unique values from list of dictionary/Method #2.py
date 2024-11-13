# Python3 code to demonstrate working of
# Get Unique values from list of dictionary
# Using set() + values() + from_iterable()
from itertools import chain

# Initialize list
test_list = [{'gfg': 1, 'is': 2}, {'best': 1, 'for': 3}, {'CS': 2}]

# printing original list
print("The original list : " + str(test_list))

# Using set() + values() + from_iterable()
# Get Unique values from list of dictionary
res = list(set(chain.from_iterable(sub.values() for sub in test_list)))

# printing result
print("The unique values in list are : " + str(res))
