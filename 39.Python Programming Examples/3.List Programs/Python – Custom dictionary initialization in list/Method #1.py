# Python3 code to demonstrate working of
# Custom dictionary initialization in list
# using {dict} + "*" operator

# Initialize dict
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# Custom dictionary initialization in list
# using {dict} + "*" operator
res = [test_dict] * 6

print("The list of custom dictionaries is : " + str(res))
