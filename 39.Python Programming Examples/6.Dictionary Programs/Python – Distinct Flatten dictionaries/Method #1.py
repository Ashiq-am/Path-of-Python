# Python3 code to demonstrate working of
# Distinct Flatten dictionaries
# Using loop + isinstance() + list comprehension

def flatten(temp_dict, temp_list):
	for key, val in temp_dict.items():
		if isinstance(val, dict):
			temp_list.append(key)
			flatten(val, temp_list)
		else:
			temp_list.extend([key, val])
	return temp_list

# initializing dictionary
test_dict = {'gfg' : {'is' : 4, "best" : 10}, 'is' : {'for' : { 'geeks' : 8 }}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Distinct Flatten dictionaries
# Using loop + isinstance() + list comprehension
res = [flatten(val, [key]) for key, val in test_dict.items()]

# printing result
print("The flattened dictionary elements : " + str(res))
