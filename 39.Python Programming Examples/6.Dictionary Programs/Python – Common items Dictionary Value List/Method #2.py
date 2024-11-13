# Python3 code to demonstrate
# Common elements Dictionary Value List
# using dictionary comprehension + set operations

# initializing dicts
test_dict1 = { "Key1" : [1, 3, 4], "key2" : [4, 5] }
test_dict2 = { "Key1" : [1, 7, 3] }

# printing original dicts
print("The original dict 1 : " + str(test_dict1))
print("The original dict 2 : " + str(test_dict2))

# using dictionary comprehension + set operations
# Common elements Dictionary Value List
res = {key : list(set(set(test_dict1.get(key, [])) & set(test_dict2.get(key, []))))
	for key in set(test_dict2) & set(test_dict1)}

# print result
print("The dicts after intersection is : " + str(res))
