# Python3 code to demonstrate working of
# Random uppercase in Strings
# Using join() + choice() + upper() + lower()
from random import choice

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# choosing from upper or lower for each character
res = ''.join(choice((str.upper, str.lower))(char) for char in test_str)

# printing result
print("Random Uppercased Strings : " + str(res))
