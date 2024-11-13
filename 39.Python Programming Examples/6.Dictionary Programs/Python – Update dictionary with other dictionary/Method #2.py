# Python3 code to demonstrate working of
# Update dictionary with other dictionary
# Using dictionary comprehension

# initializing dictionaries
test_dict1 = {'gfg' : 1, 'best' : 2, 'for' : 4, 'geeks' : 6}
test_dict2 = {'for' : 3, 'geeks' : 5}

# printing original dictionaries
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# Update dictionary with other dictionary
# Using dictionary comprehension
res = {key : test_dict2.get(key, val) for key, val in test_dict1.items()}

# printing result
print("The updated dictionary is : " + str(res))
