# Python3 code to demonstrate working of
# Selective Keys Summation
# Using list comprehension + get() + sum()

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'CS': 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize key list
key_list = ['gfg', 'best', 'CS']

# Using list comprehension + get() + sum()
# Selective Keys Summation
res = sum([test_dict.get(key) for key in key_list])

# printing result
print("The summation of Selective keys : " + str(res))
