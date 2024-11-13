# Python3 code to demonstrate working of
# Test if element is dictionary value
# Using in operator and values()

# initializing dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Test if element is dictionary value
# Using in operator and values()
res = 3 in test_dict.values()

# printing result
print("Is 3 present in dictionary : " + str(res))
