# Python3 code to demonstrate working of
# Concatenate similar set keys in Dictionary
# Using defauldict() + join()
from collections import defaultdict

# initializing dictionary
test_dict = {'gfg': {5, 4, 3}, 'is': {4, 3, 5}, 'best': {
	1, 4, 3}, 'for': {1, 3, 4}, 'geeks': {1, 2, 3}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

hash_vals = defaultdict(list)
for key, val in test_dict.items():

	# values are hashed using frozenset
	hash_vals[frozenset(val)].append(key)

# perform joining
res = {'-'.join(keys): vals for (vals, keys) in hash_vals.items()}

# printing result
print("The concatenated keys : " + str(res))
