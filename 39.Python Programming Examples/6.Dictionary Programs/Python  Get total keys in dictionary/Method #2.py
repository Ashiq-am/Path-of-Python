# Python3 code to demonstrate working of
# Get total keys in dictionary
from collections import Mapping

# Utility function to perform task
def total_keys(test_dict):
	for key, value in test_dict.items():
		if isinstance(value, Mapping):
			yield from total_keys(value)
	yield len(test_dict)

# Initialize dictionary
test_dict = { 'gfg' : { 'is' : 1, 'best' : { 'for' : {'geeks' :4}}}}

# Printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using yield() + recursion
# Get total keys in dictionary
res = sum(total_keys(test_dict))

# printing result
print("Number of keys in dictionary is : " + str(res))
