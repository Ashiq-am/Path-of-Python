# Python3 code to demonstrate
# occurrence frequency using
# re + findall()
import re

# initializing string
test_str = "GeeksforGeeks"

# using re + findall() to get count
# counting e
count = len(re.findall("e", test_str))

# printing result
print ("Count of e in GeeksforGeeks is : " + str(count))
