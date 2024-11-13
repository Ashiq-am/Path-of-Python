# Python3 code to demonstrate working of
# Check if all values are 0 in dictionary
# Using any() + not operator

# Initialize dictionary
test_dict = {'gfg' : 0, 'is' : 1, 'best' : 0}

# Printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using any() + not operator
# Check if all values are 0 in dictionary
res = not any(test_dict.values())

# printing result
print("Does all keys have 0 value ? : " + str(res))
