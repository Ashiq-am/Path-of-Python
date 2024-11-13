# Python3 code to demonstrate working of
# Get all tuple keys from dictionary
# Using list comprehension

# Initializing dict
test_dict = {(5, 6) : 'gfg', (1, 2, 8) : 'is', (9, 10) : 'best'}

# printing original dict
print("The original dict is : " + str(test_dict))

# Get all tuple keys from dictionary
# Using list comprehension
res = [ele for key in test_dict for ele in key]

# printing result
print("The dictionary tuple key elements are : " + str(res))
