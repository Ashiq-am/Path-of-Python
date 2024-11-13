# Python3 code to demonstrate working of
# Check for Non None Dictionary values
# Using in operator + values()

# initializing dictionary
test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : None}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using in operator + values()
# Check for Non None Dictionary values
res = None in test_dict.values()

# printing result
print("Does Dictionary contain None value ? " + str(res))
