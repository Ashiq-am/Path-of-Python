# Python3 code to demonstrate
# Union of Value Lists
# using loops

# initializing dicts
test_dict1 = { "Key1" : [1, 3, 4], "key2" : [4, 5] }
test_dict2 = { "Key1" : [1, 7, 8] }

# printing original dicts
print("The original dict 1 : " + str(test_dict1))
print("The original dict 2 : " + str(test_dict2))

# using loops
# Union of Value Lists
for key in test_dict1:
	if key in test_dict2:
		for val in test_dict1[key]:
			if val not in test_dict2[key]:
				test_dict2[key].append(val)
	else:
		test_dict2[key] = test_dict1[key][:]

# print result
print("The dicts after union is : " + str(test_dict2))
