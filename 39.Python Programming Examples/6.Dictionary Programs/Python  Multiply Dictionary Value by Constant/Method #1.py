# Python3 code to demonstrate working of
# Multiply Dictionary Value by Constant
# Using get()

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'for': 4, 'CS': 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize K
K = 5

# Using get()
# Multiply Dictionary Value by Constant
test_dict['best'] = test_dict.get('best', 1) * K

# printing result
print("Dictionary after the multiplication of key : " + str(test_dict))
