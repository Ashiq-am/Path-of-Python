# Python3 code to demonstrate working of
# Convert Dictionary to Concatenated String
# Using reduce() + lambda
from functools import reduce

# initializing dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Dictionary to Concatenated String
# Using reduce() + lambda
res = reduce(lambda key, val : key + str(val[0]) + str(val[1]), test_dict.items(), '')

# printing result
print("The dictionary after concatenation is : " + str(res))
