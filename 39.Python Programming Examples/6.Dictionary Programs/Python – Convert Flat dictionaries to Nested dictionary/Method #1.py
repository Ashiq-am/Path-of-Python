# Python3 code to demonstrate working of
# Convert Flat dictionaries to Nested dictionary
# Using key access + dict()

# initializing dictionaries
test_dict1 = {'gfg' : 1, 'best' : 2}
test_dict2 = {'for' : 3, 'geeks' : 5}

# printing original dictionaries
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# Convert Flat dictionaries to Nested dictionary
# Using key access + dict()
res = dict()
res["level1"] = test_dict1
res['level2'] = test_dict2

# printing result
print("The nested dictionary is : " + str(res))
