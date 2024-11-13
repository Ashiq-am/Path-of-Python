# Python3 code to demonstrate working of
# Consecutive Alphabetic Occurrence
# Using list comprehension + ascii_letters + zip()
from string import ascii_letters

# initializing string
test_str = 'geeksforgeeks is best fgr geeks'

# printing original string
print("The original string is : " + str(test_str))

# Consecutive Alphabetic Occurrence
# Using list comprehension + ascii_letters + zip()
res = [(i, j) for i, j in zip(ascii_letters,
	ascii_letters[1:]) if i + j in test_str]

# printing result
print("The Consecutive matching letter pairs : " + str(res))
