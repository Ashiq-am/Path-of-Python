# Python3 code to demonstrate working of
# Uppercase Nth character
# Using upper() + string slicing + lambda

# initializing string
test_str = "GeeksforGeeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing N
N = 4

# Using upper() + string slicing + lambda
# Uppercase Nth character
res = lambda test_str: test_str[:N] + test_str[N].upper() + test_str[N + 1:] if test_str else ''

# printing result
print("The string after uppercasing initial character : " + str(res(test_str)))
