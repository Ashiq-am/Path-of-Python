# Python3 code to demonstrate working of
# Add space between Numbers and Alphabets in String
# using regex + sub() + lambda
import re

# initializing string
test_str = 'geeks4geeks is1for10geeks'

# printing original String
print("The original string is : " + str(test_str))

# using sub() to solve the problem, lambda used tp add spaces
res = re.sub("[A-Za-z]+", lambda ele: " " + ele[0] + " ", test_str)

# printing result
print("The space added string : " + str(res))
