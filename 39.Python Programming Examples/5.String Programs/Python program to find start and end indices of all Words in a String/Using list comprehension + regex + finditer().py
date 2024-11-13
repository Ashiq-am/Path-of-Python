# Python3 code to demonstrate working of
# Word Ranges in String
# Using list comprehension + regex + finditer()
import re

# initializing string
test_str = ' Geekforgeeks is Best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# regex to get words, loop to get each start and end index
res = [(ele.start(), ele.end() - 1) for ele in re.finditer(r'\S+', test_str)]

# printing result
print("Word Ranges are : " + str(res))
