# Python3 code to demonstrate working of
# Get first K items in dictionary
# Using items() + list slicing

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'CS': 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize limit
K = 3

# Using items() + list slicing
# Get first K items in dictionary
res = dict(list(test_dict.items())[0: K])

# printing result
print("Dictionary limited by K is : " + str(res))
