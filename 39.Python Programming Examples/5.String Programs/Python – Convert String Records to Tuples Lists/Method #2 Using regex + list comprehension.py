# Python3 code to demonstrate working of
# Convert String Records to Tuples Lists
# Using regex + list comprehension
import re

# initializing string
test_str = '[(gfg, ), (is, ), (best, )]'

# printing original string
print("The original string is : " + test_str)

# Convert String Records to Tuples Lists
# Using regex + list comprehension
regex = re.compile(r'\((.*?)\)')
temp = regex.findall(test_str)
res = [tuple(sub.split(', ')) for sub in temp]

# printing result
print("The list of Tuples is : " + str(res))
