# Python3 code to demonstrate working of
# Least Value test in Dictionary
# Using all() + dictionary comprehension

# Initialize dictionary
test_dict = {'gfg' : 8, 'is' : 10, 'best' : 11}

# Printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Initialize K
K = 8

# using all() + dictionary comprehension
# Least Value test in Dictionary
res = all(x >= K for x in test_dict.values())

# printing result
print("Does all keys have atleast K value ? : " + str(res))
