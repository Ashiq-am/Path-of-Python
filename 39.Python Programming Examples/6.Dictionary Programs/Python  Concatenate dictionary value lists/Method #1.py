# Python3 code to demonstrate working of
# Concatenating dictionary value lists
# Using sum() + values()

# initializing dictionary
test_dict = {"Gfg" : [4, 5], "is" : [6, 8], "best" : [10]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Concatenating dictionary value lists
# Using sum() + values()
res = sum(test_dict.values(), [])

# printing result
print("The Concatenated list values are : " + str(res))
