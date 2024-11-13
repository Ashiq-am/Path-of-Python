# Python3 code to demonstrate working of
# Multiplication across Like Keys Value list elements
# Using dictionary comprehension + zip()

# initializing dictionaries
test_dict1 = {"Gfg" : [4, 6, 7], "Best" : [8, 6, 4], "is" : [9, 3, 4]}
test_dict2 = {"Gfg": [8, 4, 3], "Best" : [6, 3, 1], "is" : [9, 8, 2]}

# printing original lists
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# Using zip() to perform link keys and values
res = {key: [ele1 * ele2 for (ele1, ele2) in zip(test_dict1[key], val2)]
	for (key, val2) in zip(test_dict1.keys(), test_dict2.values())}

# printing result
print("The constructed dictionary : " + str(res))
