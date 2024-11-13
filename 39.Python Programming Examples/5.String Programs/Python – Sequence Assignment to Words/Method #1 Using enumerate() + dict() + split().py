# Python3 code to demonstrate working of
# Sequence Assignment to Words
# Using split() + enumerate() + dict()

# initializing string
test_str = 'geekforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# using dict() to convert result in idx:word manner
res = dict(enumerate(test_str.split()))

# printing result
print("The Assigned Sequence : " + str(res))
