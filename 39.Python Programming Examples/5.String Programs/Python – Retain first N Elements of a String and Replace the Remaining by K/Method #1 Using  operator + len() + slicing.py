# Python3 code to demonstrate working of
# Retain N and Replace remaining by K
# Using * operator + len() + slicing

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing length needed
N = 4

# initializing remains char
K = "@"

# using len() and * operator to solve problem
res = test_str[:N] + K * (len(test_str) - N)

# printing result
print("The resultant string : " + str(res))
