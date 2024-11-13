# Python3 code to demonstrate working of
# Kth Character Lowercase
# Using lower() + string slicing

# initializing string
test_str = "GEEKSFORGEEKS"

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 4

# Using lower() + string slicing
# Kth Character Lowercase
res = test_str[:K] + test_str[K].lower() + test_str[K + 1:]

# printing result
print("The string after lowercasing Kth character : " + str(res))
