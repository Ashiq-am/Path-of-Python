# Python3 code to demonstrate working of
# Ways to extract all dictionary values
# Using loop + keys()

# initializing dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extracting all dictionary values
# Using loop + keys()
res = []
for key in test_dict.keys() :
	res.append(test_dict[key])

# printing result
print("The list of values is : " + str(res))
