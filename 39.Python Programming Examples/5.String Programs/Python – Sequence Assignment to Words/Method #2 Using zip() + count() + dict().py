# Python3 code to demonstrate working of
# Sequence Assignment to Words
# Using zip() + count() + dict()
from itertools import count

# initializing string
test_str = 'geekforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# using dict() to convert result in idx:word manner
# count() from itertools used for this task
res = dict(zip(count(), test_str.split()))

# printing result
print("The Assigned Sequence : " + str(res))
