# Python3 code to demonstrate working of
# Keys Frequency with Value atmost K
# Using sum() + values()

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'CS': 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize value
K = 3

# Using sum() + values()
# Keys Frequency with Value atmost K
res = sum(x <= K for x in test_dict.values())

# printing result
print("Frequency of keys with values till K is : " + str(res))
