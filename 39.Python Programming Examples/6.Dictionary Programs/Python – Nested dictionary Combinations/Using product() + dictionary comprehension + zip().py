# Python3 code to demonstrate working of
# Nested dictionary Combinations
# Using product() + dictionary comprehension + zip()
from itertools import product

# initializing dictionary
test_dict = {'gfg': {'is' : [6, 7, 8], 'best': [1, 9, 4]}}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Nested dictionary Combinations
# Using product() + dictionary comprehension + zip()
res = { key + str(j) : dict(zip(val.keys(), k))
		for key, val in test_dict.items()
		for j, k in enumerate(product(*val.values()))}

# printing result
print("The possible combinations : " + str(res))
