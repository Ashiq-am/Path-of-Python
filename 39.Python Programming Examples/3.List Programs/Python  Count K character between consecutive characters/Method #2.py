# Python3 code to demonstrate working of
# Count K character between consecutive characters
# Using list comprehension + findall()
import re

# initializing string
test_str = "g---f--g-i--s----b--e----s---t"

# printing original string
print("The original string is : " + test_str)

# Count K character between consecutive characters
# Using list comprehension + findall()
res = [len(ele) for ele in re.findall('(?<=[a-z])-*(?=[a-z])', test_str)]

# printing result
print("List of character count : " + str(res))
