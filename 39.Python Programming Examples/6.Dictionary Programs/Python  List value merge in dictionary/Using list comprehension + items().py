# Python3 code to demonstrate working of
# List value merge in dictionary
# Using items() + list comprehension

# initializing dictionaries
test_dict1 = {'Gfg' : [1, 2, 3], 'for' : [2, 4], 'CS' : [7, 8]}
test_dict2 = {'Gfg' : [10, 11], 'for' : [5], 'CS' : [0, 18]}

# printing original dictionaries
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# Using items() + list comprehension
# List value merge in dictionary
res = {key: value + test_dict2[key] for key, value in test_dict1.items()}

# printing result
print("The merged dictionary is : " + str(res))
