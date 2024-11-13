# Python3 code to demonstrate working of
# Dictionary Values Division
# Using dictionary comprehension + keys()

# Initialize dictionaries
test_dict1 = {'gfg' : 20, 'is' : 24, 'best' : 100}
test_dict2 = {'gfg' : 10, 'is' : 6, 'best' : 10}

# printing original dictionaries
print("The original dictionary 1 : " + str(test_dict1))
print("The original dictionary 2 : " + str(test_dict2))

# Using dictionary comprehension + keys()
# Dictionary Values Division
res = {key: test_dict1[key] // test_dict2.get(key, 0)
						for key in test_dict1.keys()}

# printing result
print("The divided dictionary is : " + str(res))
