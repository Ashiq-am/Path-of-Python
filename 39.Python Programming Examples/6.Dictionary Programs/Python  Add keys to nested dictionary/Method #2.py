# Python3 code to demonstrate working of
# Update nested dictionary keys
# Using update()

# initializing dictionaries
test_dict = {'GFG' : {'rate' : 4, 'since' : 2012}}
upd_dict = {'rank' : 1, 'popularity' : 5}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using update()
# Update nested dictionary keys
test_dict['GFG'].update(upd_dict)

# printing result
print("Dictionary after nested key update : " + str(test_dict))
