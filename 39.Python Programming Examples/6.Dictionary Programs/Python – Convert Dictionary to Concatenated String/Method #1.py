# Python3 code to demonstrate working of
# Convert Dictionary to Concatenated String
# Using join() + items()

# initializing dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Dictionary to Concatenated String
# Using join() + items()
res = ''.join(key + str(val) for key, val in test_dict.items())

# printing result
print("The dictionary after concatenation is : " + str(res))
