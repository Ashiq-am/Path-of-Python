# Python3 code to demonstrate working of
# Alphabets Frequency in String
# Using ascii_uppercase() + ascii_lowercase() + len()
import string

# initializing string
test_str = 'geeksforgeeks !!$ is best 4 all Geeks 10-0'

# printing original string
print("The original string is : " + str(test_str))

# ascii_lowercase and ascii_uppercase
# to check for Alphabets
res = len([ele for ele in test_str if ele in string.ascii_uppercase or ele in string.ascii_lowercase])

# printing result
print("Count of Alphabets : " + str(res))
