# Python3 code to demonstrate working of
# Getting first key in dictionary
# Using next() + iter()

# initializing dictionary
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using next() + iter()
# Getting first key in dictionary
res = next(iter(test_dict))

# printing initial key
print("The first key of dictionary is : " + str(res))
