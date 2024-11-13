# Python3 code to demonstrate working of
# Count keys with particular value in dictionary
# Using sum() + values()

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'best': 3, 'for': 2, 'CS': 2}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize value
K = 2

# Using sum() + values()
# Selective key values in dictionary
res = sum(x == K for x in test_dict.values())

# printing result
print("Frequency of K is : " + str(res))
