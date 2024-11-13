# Python3 code to demonstrate working of
# Dictionary items in value range
# Using loop

# initializing dictionary
test_dict = {'Gfg' : 6, 'is' : 7, 'best' : 9, 'for' : 8, 'geeks' : 11}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing range
i, j = 8, 12

# using loop to iterate through all keys
res = dict()
for key, val in test_dict.items():
	if int(val) >= i and int(val) <= j:
		res[key] = val

# printing result
print("The extracted dictionary : " + str(res))
