# Python3 code to demonstrate working of
# Increment value in dictionary
# Using get()

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'for': 4, 'CS': 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using get()
# Increment value in dictionary
test_dict['best'] = test_dict.get('best', 0) + 3

# printing result
print("Dictionary after the increment of key : " + str(test_dict))
