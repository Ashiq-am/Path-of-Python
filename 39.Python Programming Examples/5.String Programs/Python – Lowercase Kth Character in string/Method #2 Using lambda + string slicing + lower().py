# Python3 code to demonstrate working of
# Kth Character Lowercase
# Using lower() + string slicing + lambda

# initializing string
test_str = "GEEKSFORGEEKS"

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 4

# Using lower() + string slicing + lambda
# Kth Character Lowercase
res = lambda test_str: test_str[:K] + test_str[K].lower() + test_str[K + 1:] if test_str else ''

# printing result
print("The string after lowercasing initial character : " + str(res(test_str)))
