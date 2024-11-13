# Python3 code to demonstrate working of
# Lowercase first character of String
# Using lower() + string slicing + lambda

# initializing string
test_str = "GeeksforGeeks"

# printing original string
print("The original string is : " + str(test_str))

# Using lower() + string slicing + lambda
# Lowercase first character of String
res = lambda test_str: test_str[:1].lower() + test_str[1:] if test_str else ''

# printing result
print("The string after lowercasing initial character : " + str(res(test_str)))
