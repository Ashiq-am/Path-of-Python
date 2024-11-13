# Python3 code to demonstrate working of
# Distance between occurrences
# Using find() + rfind()

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 'k'

# Distance between occurrences
# Using find() + rfind()
res = test_str.rfind(K) - test_str.find(K)

# printing result
print("The character occurrence difference is : " + str(res))
