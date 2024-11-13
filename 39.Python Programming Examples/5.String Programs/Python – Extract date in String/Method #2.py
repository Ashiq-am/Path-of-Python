# Python3 code to demonstrate working of
# Detect date in String
# Using python-dateutil()
from dateutil import parser

# initializing string
test_str = "gfg at 2021-01-04"

# printing original string
print("The original string is : " + str(test_str))

# extracting date using inbuilt func.
res = parser.parse(test_str, fuzzy=True)

# printing result
print("Computed date : " + str(res)[:10])
