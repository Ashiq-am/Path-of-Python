# Python3 code to demonstrate working of
# Selective key values in dictionary
# Using list comprehension + get()

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'CS': 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize key list
key_list = ['gfg', 'best', 'CS']

# Using list comprehension + get()
# Selective key values in dictionary
res = [test_dict.get(key) for key in key_list]

# printing result
print("The values of Selective keys : " + str(res))
