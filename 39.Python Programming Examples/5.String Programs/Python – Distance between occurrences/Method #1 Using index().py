# Python3 code to demonstrate working of
# Distance between occurrences
# Using index()

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 'k'

# Distance between occurrences
# Using index()
res = test_str.index(K, test_str.index(K) + 1) - test_str.index(K)

# printing result
print("The character occurrence difference is : " + str(res))
