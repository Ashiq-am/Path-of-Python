# Python3 code to demonstrate working of
# Characters Index occurrences in String
# Using regex + set() + list comprehension + replace()
import re

# initializing string
test_str = "Gfg is best for geeks"

# printing original string
print("The original string is : " + test_str)

# Characters Index occurrences in String
# Using regex + set() + list comprehension + replace()
temp = set(test_str.replace(' ', ''))
res = {ele: [sub.start() for sub in re.finditer(ele, test_str)] for ele in temp}

# printing result
print("Characters frequency index dictionary : " + str(res))
