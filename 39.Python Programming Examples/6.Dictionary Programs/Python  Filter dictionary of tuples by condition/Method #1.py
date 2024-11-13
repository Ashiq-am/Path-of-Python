# Python3 code to demonstrate working of
# Filter dictionary of tuples by condition
# Using items() + dictionary comprehension

# initializing dictionary
test_dict = {'a' : (6, 3), 'b' : (4, 8), 'c' : (8, 4)}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Filter dictionary of tuples by condition
# Using items() + dictionary comprehension
res = {key: val for key, val in test_dict.items() if val[0] >= 6 and val[1] <= 4}

# printing result
print("The filtered dictionary is : " + str(res))
