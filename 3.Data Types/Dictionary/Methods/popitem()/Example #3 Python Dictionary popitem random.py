# Python3 code to demonstrate working of
# Get random dictionary pair in dictionary
# Using popitem()

# Initialize dictionary
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Get random dictionary pair in dictionary
# Using popitem()
res = test_dict.popitem()

# printing result
print("The random pair is : " + str(res))
