# Python3 code to demonstrate working of
# Unpacking dictionary keys into tuple
# Using tuple()

# initializing dictionary
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using tuple()
# Unpacking dictionary keys into tuple
res = tuple(test_dict)

# printing result
print("The unpacked dict. keys into tuple is : " + str(res))
