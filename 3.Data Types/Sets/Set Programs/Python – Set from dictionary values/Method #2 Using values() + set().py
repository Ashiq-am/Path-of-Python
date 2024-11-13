# Python3 code to demonstrate working of
# Set from dictionary values
# Using values() + set()

# initializing dictionary
test_dict = {'Gfg': 4, 'is': 3, 'best': 7, 'for': 3, 'geek': 4}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# values() used to get values
res = set(test_dict.values())

# printing result
print("The converted set : " + str(res))
