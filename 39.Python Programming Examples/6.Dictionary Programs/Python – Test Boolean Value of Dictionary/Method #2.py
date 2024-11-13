# Python3 code to demonstrate working of
# Test Boolean Value of Dictionary
# Using all() + values()

# initializing dictionary
test_dict = {'gfg' : True, 'is' : False, 'best' : True}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Test Boolean Value of Dictionary
# Using all() + values()
res = all(test_dict.values())

# printing result
print("Is Dictionary True ? : " + str(res))
