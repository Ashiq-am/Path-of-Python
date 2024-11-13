# Python3 code to demonstrate working of
# Split String on all punctuations
# using regex + findall()
import re

# initializing string
test_str = 'geeksforgeeks ! is-best, for @geeks'

# printing original String
print("The original string is : " + str(test_str))

# using findall() to get all regex matches.
res = re.findall( r'\w+|[^\s\w]+', test_str)

# printing result
print("The converted string : " + str(res))
