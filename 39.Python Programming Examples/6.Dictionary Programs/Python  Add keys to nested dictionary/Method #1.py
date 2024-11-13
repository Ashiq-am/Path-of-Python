# Python3 code to demonstrate working of
# Update nested dictionary keys
# Using dictionary brackets

# initializing dictionary
test_dict = {'GFG' : {'rate' : 4, 'since' : 2012}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using dictionary brackets
# Update nested dictionary keys
test_dict['GFG']['rank'] = 1

# printing result
print("Dictionary after nested key update : " + str(test_dict))
