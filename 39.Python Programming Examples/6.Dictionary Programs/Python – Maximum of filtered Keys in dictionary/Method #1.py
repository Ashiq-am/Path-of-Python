# Python3 code to demonstrate working of
# Maximum of filtered Keys
# Using list comprehension + get() + max()

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'CS': 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize key list
key_list = ['gfg', 'best', 'CS']

# Using list comprehension + get() + max()
# Maximum of filtered Keys
res = max([test_dict.get(key) for key in key_list])

# printing result
print("The maximum of Selective keys : " + str(res))
