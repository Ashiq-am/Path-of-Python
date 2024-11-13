# Python3 code to demonstrate working of
# Distinct Flatten dictionaries
# Using yield + isinstance()

def flatten(temp_dict):
	if isinstance(temp_dict, dict):
		for key, val in temp_dict.items():
			yield key
			yield from flatten(val)
	else:
		yield temp_dict

# initializing dictionary
test_dict = {'gfg' : {'is' : 4, "best" : 10}, 'is' : {'for' : { 'geeks' : 8 }}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Distinct Flatten dictionaries
# Using yield + isinstance()
res = [[key, *flatten(val)] for key, val in test_dict.items()]

# printing result
print("The flattened dictionary elements : " + str(res))
