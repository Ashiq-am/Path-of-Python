# Python3 code to demonstrate
# converting hexadecimal string to decimal
# Using ast.literal_eval()
from ast import literal_eval

# initializing string
test_string = '0xA'

# printing original string
print("The original string : " + str(test_string))

# using ast.literal_eval()
# converting hexadecimal string to decimal
res = literal_eval(test_string)

# print result
print("The decimal number of hexadecimal string : " + str(res))
