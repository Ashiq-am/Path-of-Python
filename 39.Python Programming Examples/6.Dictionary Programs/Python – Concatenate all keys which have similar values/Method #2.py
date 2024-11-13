# Python3 code to demonstrate working of
# Concatenate similar set keys in Dictionary
# Using groupby() + join() + dictionary comprehension
from itertools import groupby

# initializing dictionary
test_dict = {'gfg': {5, 4, 3}, 'is': {4, 3, 5},
			'best': {1, 4, 3}, 'for': {1, 3, 4},
			'geeks': {1, 2, 3}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# elements grouped using groupby()
# dictionary comprehension provides shorthand to perform grouping
res = {'-'.join(val): key for key, val in groupby(
sorted(test_dict, key=test_dict.get), key=lambda sub: test_dict[sub])}

# printing result
print("The concatenated keys : " + str(res))
