# Python3 code to demonstrate working of
# Search Key from Value
# Using naive method

# initializing dictionary
test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing value
val = 3

# Using naive method
# Search key from Value
for key in test_dict:
	if test_dict[key] == val:
		res = key

# printing result
print("The key correspoding to value : " + str(res))
