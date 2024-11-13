# Python3 code to demonstrate working of
# Split joined consecutive similar characters
# Using join() + list comprehension + groupby()
from itertools import groupby

# initializing string
test_str = 'ggggffggisssbbbeessssstt'

# printing original string
print("The original string is : " + str(test_str))

# groupby groups the elements, join joining Consecutive groups
res = ["".join(grup) for ele, grup in groupby(test_str)]

# printing result
print("Consecutive split string is : " + str(res))
