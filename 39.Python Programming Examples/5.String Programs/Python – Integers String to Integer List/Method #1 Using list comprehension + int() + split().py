# Python3 code to demonstrate working of
# Integers String to Integer List
# Using list comprehension + int() + split()
import string

# initializing string
test_str = '4 5 -3 2 -100 -2 -4 9'

# printing original string
print("The original string is : " + str(test_str))

# int() converts to required integers
res = [int(ele) for ele in test_str.split()]

# printing result
print("Converted Integers : " + str(res))
