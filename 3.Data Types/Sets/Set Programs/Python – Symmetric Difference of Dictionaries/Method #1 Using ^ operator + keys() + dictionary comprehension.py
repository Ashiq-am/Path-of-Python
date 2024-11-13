# Python3 code to demonstrate working of
# Symmetric Difference of Dictionaries
# Using ^ operator + keys() + dictionary comprehension

# initializing dictionaries
test_dict1 = {'Gfg': 4, 'is': 3, 'best': 7, 'for': 3, 'geek': 4}
test_dict2 = {'Gfg': 4, 'is': 3, 'good': 7, 'for': 3, 'all': 4}

# printing original dictionaries
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# getting symmetric difference using ^ operation
res = {key: test_dict1[key] if key in test_dict1 else test_dict2[key]
	for key in test_dict1.keys() ^ test_dict2.keys()}

# printing result
print("The symmetric difference : " + str(res))
