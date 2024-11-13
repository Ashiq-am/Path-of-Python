# Python3 code to demonstrate working of
# Get all tuple keys from dictionary
# Using chain.from_iterable()
from itertools import chain

# Initializing dict
test_dict = {(5, 6) : 'gfg', (1, 2, 8) : 'is', (9, 10) : 'best'}

# printing original dict
print("The original dict is : " + str(test_dict))

# Get all tuple keys from dictionary
# Using chain.from_iterable()
res = list(chain.from_iterable(test_dict))

# printing result
print("The dictionary tuple key elements are : " + str(res))
