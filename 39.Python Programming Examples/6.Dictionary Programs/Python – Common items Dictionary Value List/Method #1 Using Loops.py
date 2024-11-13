# Python3 code to demonstrate
# Common elements Dictionary Value List
# using loops

# initializing dicts
test_dict1 = { "Key1" : [1, 3, 4], "key2" : [4, 5] }
test_dict2 = { "Key1" : [1, 7, 3] }

# printing original dicts
print("The original dict 1 : " + str(test_dict1))
print("The original dict 2 : " + str(test_dict2))

# using loops
# Common elements Dictionary Value List
res = dict()
for key in test_dict1:
	if key in test_dict2:
		res[key] = []
		for val in test_dict1[key]:
			if val in test_dict2[key]:
				res[key].append(val)

# print result
print("The dicts after intersection is : " + str(res))
