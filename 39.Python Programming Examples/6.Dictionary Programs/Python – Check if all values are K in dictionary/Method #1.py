# Python3 code to demonstrate working of
# Test if all values are K in dictionary
# Using all() + dictionary comprehension

# Initialize dictionary
test_dict = {'gfg' : 8, 'is' : 8, 'best' : 8}

# Printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Initialize K
K = 8

# using all() + dictionary comprehension
# Test if all values are K in dictionary
res = all(x == K for x in test_dict.values())

# printing result
print("Does all keys have K value ? : " + str(res))
