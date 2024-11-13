# Python3 code to demonstrate working of
# Search Key from Value
# Using items() + list comprehension

# initializing dictionary
test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing value
val = 3

# Using items() + list comprehension
# Search key from Value
res = [key for key, value in test_dict.items() if value == val]

# printing result
print("The key correspoding to value : " + str(res))
