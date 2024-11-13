# Python3 code to demonstrate working of
# Get next key in Dictionary
# Using iter() + next()

# initializing dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing key
test_key = 'is'

# Get next key in Dictionary
# Using iter() + next()
res = None
temp = iter(test_dict)
for key in temp:
	if key == test_key:
		res = next(temp, None)

# printing result
print("The next key is : " + str(res))
