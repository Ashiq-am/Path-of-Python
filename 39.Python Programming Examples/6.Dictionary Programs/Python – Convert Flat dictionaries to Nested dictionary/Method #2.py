# Python3 code to demonstrate working of
# Convert Flat dictionaries to Nested dictionary
# Using zip()

# initializing dictionaries
test_dict1 = {'gfg' : 1, 'best' : 2}
test_dict2 = {'for' : 3, 'geeks' : 5}

# printing original dictionaries
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# Convert Flat dictionaries to Nested dictionary
# Using zip()
key_dict = ['level1', 'level2']
dict_list = [test_dict1, test_dict2]
res = dict(zip(key_dict, dict_list))

# printing result
print("The nested dictionary is : " + str(res))
