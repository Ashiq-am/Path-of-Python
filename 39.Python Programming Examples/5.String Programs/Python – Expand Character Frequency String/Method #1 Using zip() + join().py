# Python3 code to demonstrate working of
# Expand Character Frequency String
# Using join() + zip()
import re

# initializing string
test_str = 'g7f2g3i2s2b3e4s5t6'

# printing original string
print("The original string is : " + str(test_str))

# using zip() to pair up numbers and characters
# seperately
res = "".join(a *int(b) for a, b in zip(test_str[0::2], test_str[1::2]))

# printing result
print("The expanded string : " + str(res))
