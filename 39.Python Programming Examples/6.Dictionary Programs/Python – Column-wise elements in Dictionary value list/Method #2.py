# Python3 code to demonstrate working of
# Column-wise elements in Dictionary value list
# Using chain.from_iterable() + zip() + * operator
from itertools import chain

# initializing dictionary
test_dict = {'Gfg' : [3, 6, 7],
			'is' : [4, 2, 6],
			'best' :[9, 1, 3]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# values() gets all values at on
res = list(chain.from_iterable(zip(*test_dict.values())))

# printing result
print("The extracted values : " + str(res))
