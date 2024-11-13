# Python3 code to demonstrate working of
# Remove digits before K Number
# Using regex() + index()
import re

# initializing string
test_str = 'geeksforgeeks 2 6 is 4 geeks 5 and CS8'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 4

# using regex to achieve task
res = re.sub('[023456789]', '', test_str[0 : test_str.index(str(K))]) + test_str[test_str.index(str(K)):]

# printing result
print("String after removing digits before K : " + str(res))
