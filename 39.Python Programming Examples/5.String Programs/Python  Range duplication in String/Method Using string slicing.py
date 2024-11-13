# Python3 code to demonstrate working of
# Range duplication in String
# Using string slicing

# initializing string
test_str = "geeksforgeeks"

# printing original string
print("The original string is : " + test_str)

# initializing range
i, j = 3, 6

# Range duplication in String
# Using string slicing
temp = test_str[i:j] * 2
res = test_str[:i] + temp + test_str[j:]

# printing result
print("The string after range duplication : " + res)
