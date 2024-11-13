# Python3 code to demonstrate working of
# Change Keys Case in Dictionary
# Using isinstance() + toupper() + recursion + loop

# helper function
def keys_upper(test_dict):
	res = dict()
	for key in test_dict.keys():
		if isinstance(test_dict[key], dict):
			res[key.upper()] = keys_upper(test_dict[key])
		else:
			res[key.upper()] = test_dict[key]
	return res

# initializing dictionary
test_dict = {'Gfg' : {'a' : 5, 'b' : 6}, 'is' : {'for' :2}, 'best': 3}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Change Keys Case in Dictionary
# Using isinstance() + toupper() + recursion + loop
res = keys_upper(test_dict)

# printing result
print("The modified dictionary : " + str(res))
