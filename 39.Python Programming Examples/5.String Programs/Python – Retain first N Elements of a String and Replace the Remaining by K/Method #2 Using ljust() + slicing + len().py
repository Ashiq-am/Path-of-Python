# Python3 code to demonstrate working of
# Retain N and Replace remaining by K
# Using ljust() + slicing + len()

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing length needed
N = 4

# initializing remains char
K = "@"

# ljust assigns K to remaining string
res = test_str[:N].ljust(len(test_str), K)

# printing result
print("The resultant string : " + str(res))
