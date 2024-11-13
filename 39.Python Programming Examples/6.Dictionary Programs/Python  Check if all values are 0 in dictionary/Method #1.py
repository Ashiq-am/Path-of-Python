# Python3 code to demonstrate working of
# Check if all values are 0 in dictionary
# Using all() + dictionary comprehension

# Initialize dictionary
test_dict = {'gfg' : 0, 'is' : 0, 'best' : 0}

# Printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using all() + dictionary comprehension
# Check if all values are 0 in dictionary
res = all(x == 0 for x in test_dict.values())

# printing result
print("Does all keys have 0 value ? : " + str(res))
