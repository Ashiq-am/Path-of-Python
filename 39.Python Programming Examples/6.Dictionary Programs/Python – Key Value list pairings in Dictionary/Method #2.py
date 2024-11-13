# Python3 code to demonstrate working of
# Key Value list pairings in Dictionary
# Using dict() + zip() + product()
from itertools import product

# initializing dictionary
test_dict = {'gfg' : [7, 8],
			'best' : [10, 11, 7]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Key Value list pairings in Dictionary
# Using dict() + zip() + product()
res = [dict(zip(test_dict, sub)) for sub in product(*test_dict.values())]

# printing result
print("All key value paired List : " + str(res))
