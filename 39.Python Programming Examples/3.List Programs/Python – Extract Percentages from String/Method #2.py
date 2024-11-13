# Python3 code to demonstrate working of
# Extract Percentages from String
# Using re.sub() + split()
import re

# initializing strings
test_str = 'geeksforgeeks is 100 % way to get 200 % success'

# printing original string
print("The original string is : " + str(test_str))

# extracting words
temp = test_str.split()

# using
res = []
for sub in temp:
    if '%' in sub:
        # replace empty string to all non-number chars
        res.append(re.sub(r'[^\d, %]', '', sub))

# printing result
print("The percentages : " + str(res))
