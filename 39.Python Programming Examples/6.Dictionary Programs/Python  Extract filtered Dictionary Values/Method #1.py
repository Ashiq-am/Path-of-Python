# Python3 code to demonstrate working of
# Extract filtered Dictionary Values
# Using loop + keys()

# initializing dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 2

# Extract filtered Dictionary Values
# Using loop + keys()
res = []
for key in test_dict.keys() :
	if test_dict[key] >= K:
		res.append(test_dict[key])

# printing result
print("The list of filtered values is : " + str(res))
