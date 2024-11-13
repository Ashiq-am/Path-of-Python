# Python3 code to demonstrate working of
# Iterating through value lists dictionary
# Using list comprehension

# Initialize dictionary
test_dict = {'gfg': [1, 2], 'is': [4, 5], 'best': [7, 8]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using list comprehension
# Iterating through value lists dictionary
res = [[i for i in test_dict[x]] for x in test_dict.keys()]

# printing result
print("The list values of keys are : " + str(res))
