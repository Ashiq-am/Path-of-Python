# Python3 code to demonstrate working of
# Expand Character Frequency String
# Using regex() + join()
import re

# initializing string
test_str = 'g7f2g3i2s2b3e4s5t10'

# printing original string
print("The original string is : " + str(test_str))

# using findall to pair up numbers and characters
# seperately, can include longer digit strings
res = ''.join(chr * int(num or 1)
			for chr, num in re.findall(r'(\w)(\d+)?', test_str))

# printing result
print("The expanded string : " + str(res))
