# Python3 code to demonstrate
# how to check whether string contains
# only numbers or not
import re

# Initialising string
ini_string1 = '1234556'
ini_string2 = 'ab123bc'

# printing initial string
print("Initial Strings : ", ini_string1, ini_string2)

# Using regex()
if re.match('^[0-9]*$', ini_string1):
    print("String1 contains all numbers")
else:
    print("String1 doesn't contains all numbers")

if re.match('^[0-9]*$', ini_string2):
    print("String2 conatins all numbers")
else:
    print("String2 doesn't contains all numbers")
