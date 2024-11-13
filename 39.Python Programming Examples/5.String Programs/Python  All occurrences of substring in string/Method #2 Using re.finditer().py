# Python3 code to demonstrate working of
# All occurrences of substring in string
# Using re.finditer()
import re

# initializing string
test_str = "GeeksforGeeks is best for Geeks"

# initializing substring
test_sub = "Geeks"

# printing original string
print("The original string is : " + test_str)

# printing substring
print("The substring to find : " + test_sub)

# using re.finditer()
# All occurrences of substring in string
res = [i.start() for i in re.finditer(test_sub, test_str)]

# printing result
print("The start indices of the substrings are : " + str(res))
