# Python3 code to demonstrate working of
# Unpacking dictionary keys into tuple
# Using "=" operator and multiple variables

# initializing dictionary
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using "=" operator and multiple variables
# Unpacking dictionary keys into tuple
a, b, c = test_dict
res = a, b, c

# printing result
print("The unpacked dict. keys into tuple is : " + str(res))
