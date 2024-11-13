# Python3 code to demonstrate working of
# Convert Frequency dictionary to list
# Using list comprehension

# initializing dictionary
test_dict = {'gfg': 4, 'is': 2, 'best': 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Convert Frequency dictionary to list
# Using list comprehension
res = [[key] * test_dict[key] for key in test_dict]

# printing result
print("The resultant list : " + str(res))
