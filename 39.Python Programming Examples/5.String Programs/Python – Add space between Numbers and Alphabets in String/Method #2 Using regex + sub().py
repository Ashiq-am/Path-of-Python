# Python3 code to demonstrate working of
# Add space between Numbers and Alphabets in String
# using regex + sub()
import re

# initializing string
test_str = 'geeks4geeks is1for10geeks'

# printing original String
print("The original string is : " + str(test_str))

# using sub() to solve the problem, lambda used tp add spaces
res = re.sub('(\d+(\.\d+)?)', r' \1 ', test_str)

# printing result
print("The space added string : " + str(res))
