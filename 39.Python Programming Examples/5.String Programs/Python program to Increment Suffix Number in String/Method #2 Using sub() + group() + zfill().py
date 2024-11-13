# Python3 code to demonstrate working of
# Increment Suffix Number
# Using sub() + group() + zfill()
import re

# initializing string
test_str = 'geeks006'

# printing original string
print("The original string is : " + str(test_str))

# fstring used to form string
# zfill fills values post increment
res = re.sub(r'[0-9]+$',
             lambda x: f"{str(int(x.group()) + 1).zfill(len(x.group()))}",
             test_str)

# printing result
print("Incremented numeric String : " + str(res))
