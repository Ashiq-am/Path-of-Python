# Python3 code to demonstrate working of
# Decrement Dictionary value by K
# Using get()

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'for': 4, 'CS': 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize K
K = 5

# Using get()
# Decrement Dictionary value by K
test_dict['best'] = test_dict.get('best', 0) - K

# printing result
print("Dictionary after the decrement of key : " + str(test_dict))
