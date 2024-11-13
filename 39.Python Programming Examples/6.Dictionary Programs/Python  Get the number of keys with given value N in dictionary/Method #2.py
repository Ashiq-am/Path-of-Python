# Python3 code to Get the number of keys
# with given value N in dictionary
# Using sum() + values()

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'best': 3, 'for': 2, 'CS': 2}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize value
N = 2

# Using sum() + values()
# Selective key values in dictionary
res = sum(x == N for x in test_dict.values())

# printing result
print("Frequency of K is : " + str(res))
