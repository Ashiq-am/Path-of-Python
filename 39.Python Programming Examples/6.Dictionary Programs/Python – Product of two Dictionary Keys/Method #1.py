# Python3 code to demonstrate working of
# Dictionary Keys Product
# Using dictionary comprehension + keys()

# Initialize dictionaries
test_dict1 = {'gfg' : 6, 'is' : 4, 'best' : 7}
test_dict2 = {'gfg' : 10, 'is' : 6, 'best' : 10}

# printing original dictionaries
print("The original dictionary 1 : " + str(test_dict1))
print("The original dictionary 2 : " + str(test_dict2))

# Using dictionary comprehension + keys()
# Dictionary Keys Product
res = {key: test_dict2[key] * test_dict1.get(key, 0)
					for key in test_dict2.keys()}

# printing result
print("The product dictionary is : " + str(res))
