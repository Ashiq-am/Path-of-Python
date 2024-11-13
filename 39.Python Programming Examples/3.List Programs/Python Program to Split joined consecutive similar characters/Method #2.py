# Python3 code to demonstrate working of
# Split joined consecutive similar characters
# Using finditer() + regex + list comprehension
import re

# initializing string
test_str = 'ggggffggisssbbbeessssstt'

# printing original string
print("The original string is : " + str(test_str))

# list comprehension iterates for all the formed groups found by regex
# if consecutive numbers need to search "d" can be used.
res = [iters.group(0) for iters in re.finditer(r"(\D)\1*", test_str)]

# printing result
print("Consecutive split string is : " + str(res))
