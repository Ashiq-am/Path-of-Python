# Python3 code to demonstrate
# Extract digit string
# using re
import re

# initializing string
test_string = 'g1eeks4geeks5'

# printing original strings
print("The original string : " + test_string)

# using re
# Extract digit string
res = re.sub("\D", "", test_string)

# print result
print("The digits string is : " + str(res))
