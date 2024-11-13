# Python3 code to demonstrate
# Union of Value Lists
# using dictionary comprehension + set operations

# initializing dicts
test_dict1 = { "Key1" : [1, 3, 4], "key2" : [4, 5] }
test_dict2 = { "Key1" : [1, 7, 8] }

# printing original dicts
print("The original dict 1 : " + str(test_dict1))
print("The original dict 2 : " + str(test_dict2))

# using dictionary comprehension + set operations
# Union of Value Lists
res = {key : list(set(test_dict1.get(key, []) + test_dict2.get(key, [])))
	for key in set(test_dict2) | set(test_dict1)}

# print result
print("The dicts after union is : " + str(res))
