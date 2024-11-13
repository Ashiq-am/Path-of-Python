# Python3 code to demonstrate working of
# Convert String Matrix Representation to Matrix
# Using json.loads()
import json

# initializing string
test_str = '[["gfg", "is"], ["best", "for"], ["all", "geeks"]]'

# printing original string
print("The original string is : " + str(test_str))

# inbuild function performing task of conversion
# notice input
res = json.loads(test_str)

# printing result
print("The type of result : " + str(type(res)))
print("Converted Matrix : " + str(res))
