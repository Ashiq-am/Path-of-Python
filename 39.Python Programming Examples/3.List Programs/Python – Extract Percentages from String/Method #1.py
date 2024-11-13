# Python3 code to demonstrate working of
# Extract Percentages from String
# Using regex + findall()
import re

# initializing strings
test_str = 'geeksforgeeks is 100 % way to get 200 % success'

# printing original string
print("The original string is : " + str(test_str))

# getting required result from string
res = re.findall('\d*%', test_str)

# printing result
print("The percentages : " + str(res))
