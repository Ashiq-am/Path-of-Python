# Python3 code to demonstrate working of
# Concatenate Dictionary string values
# Using dictionary comprehension + keys()

# Initialize dictionaries
test_dict1 = {'gfg' : 'a', 'is' : 'b', 'best' : 'c'}
test_dict2 = {'gfg' : 'd', 'is' : 'e', 'best' : 'f'}

# printing original dictionaries
print("The original dictionary 1 : " + str(test_dict1))
print("The original dictionary 2 : " + str(test_dict2))

# Using dictionary comprehension + keys()
# Concatenate Dictionary string values
res = {key: test_dict1[key] + test_dict2.get(key, '') for key in test_dict1.keys()}

# printing result
print("The string concatenation of dictionary is : " + str(res))
