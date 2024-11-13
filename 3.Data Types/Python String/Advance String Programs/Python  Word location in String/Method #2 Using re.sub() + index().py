# Python3 code to demonstrate working of
# Word location in String
# Using re.sub() + index()
import re

# initializing string
test_str = 'geeksforgeeks is best for geeks'

# printing original string
print("The original string is : " + test_str)

# initializing word
wrd = 'best'

# Word location in String
# Using re.sub() + index()
res = re.sub("[^\w]", " ", test_str).split()
res = res.index(wrd) + 1

# printing result
print("The location of word is : " + str(res))
