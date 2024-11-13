# Python3 code to demonstrate working of
# Dictionary key combinations
# Using list comprehension + enumerate()

# Initializing dict
test_dict = {'gfg': 1, 'is': 2, 'the': 3, 'best': 4}

# printing original dict
print("The original dict is : " + str(test_dict))

# Dictionary key combinations
# Using list comprehension + enumerate()
test_dict = list(test_dict)
res = [(x, y) for idx, x in enumerate(test_dict) for y in test_dict[idx + 1:]]

# printing result
print("The dictionary key pair list is : " + str(res))
