# Python3 code to demonstrate working of
# Extract Keys with specific Value Type
# Using loop + isinstance()

# initializing dictionary
test_dict = {'gfg': 2, 'is': 'hello', 'best': 2, 'for': {'1': 3}, 'geeks': 4}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing type
targ_type = int

res = []
for key, val in test_dict.items():

	# checking for values datatype
	if isinstance(val, targ_type):
		res.append(key)

# printing result
print("The extracted keys : " + str(res))
