# Python3 code to demonstrate working of
# Key with all Characters in String
# Using all() + dictionary comprehension

# initializing dictionary
test_dict = { 'gfg' : ['a', 'b', 'c', 'd', 'g'],
			'is' : ['b', 'f', 'e'],
			'best' : ['c', 'd', 'g'],
			'for' : ['n', 'z'],
			'CS' : ['g', 'd'] }

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing keys
test_str = 'gd'

# Key with all Characters in String
# Using all() + dictionary comprehension
res = list({key for key, val in test_dict.items()
			if all(chr in val for chr in test_str)})

# printing result
print("The keys list : " + str(res))
