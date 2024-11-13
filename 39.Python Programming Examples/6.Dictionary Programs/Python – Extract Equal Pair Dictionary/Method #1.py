# Python3 code to demonstrate working of
# Extract Equal Pair Dictionary
# Using loop

# initializing dictionary
test_dict = { (1, 1) : 4, (2, 3) : 6, (3, 3) : 7, (5, 2) : 10, (2, 2) : 11}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extract Equal Pair Dictionary
# Using loops
res = dict()
for key, val in test_dict.items():
	if key[0] == key[1]:
		res[key[0]] = val

# printing result
print("The dictionary after equality testing : " + str(res))
