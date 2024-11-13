# Python3 code to demonstrate working of
# Updating value list in dictionary
# Using map() + lambda

# Initialize dictionary
test_dict = {'gfg': [1, 5, 6], 'is': 2, 'best': 3}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using map() + lambda
# Updating value list in dictionary
test_dict['gfg'] = list(map(lambda x: x * 2, test_dict['gfg']))

# printing result
print("Dictionary after updation is : " + str(test_dict))
