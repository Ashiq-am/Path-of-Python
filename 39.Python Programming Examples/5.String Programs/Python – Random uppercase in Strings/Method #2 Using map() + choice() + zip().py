# Python3 code to demonstrate working of
# Random uppercase in Strings
# Using map() + choice() + zip()
from random import choice

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# choosing from upper or lower for each character
# extending logic to each character using map()
res = ''.join(map(choice, zip(test_str.lower(), test_str.upper())))

# printing result
print("Random Uppercased Strings : " + str(res))
