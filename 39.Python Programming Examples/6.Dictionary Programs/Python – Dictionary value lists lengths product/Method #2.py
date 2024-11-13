# Python3 code to demonstrate working of
# Dictionary value lists lengths product
# Using map() + lambda + reduce()
from functools import reduce

# initializing dictionary
test_dict = {'Gfg' : [6, 5, 9, 3, 10],
			'is' : [1, 3, 4],
			'best' :[9, 16]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# values() used to get all lists of keys
res = reduce(lambda sub1, sub2: sub1 * sub2, map(len, test_dict.values()))

# printing result
print("The computed product : " + str(res))
