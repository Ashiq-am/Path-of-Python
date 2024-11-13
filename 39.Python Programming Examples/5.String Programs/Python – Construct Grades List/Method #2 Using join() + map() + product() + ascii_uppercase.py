# Python3 code to demonstrate working of
# Construct Grades List
# Using join() + map() + product() + ascii_uppercase
from string import ascii_uppercase
from itertools import product

# initializing N
num = 4

# Using join() + map() + product() + ascii_uppercase
# pairing using product, map used to join characters with symbols.
res = [*map(''.join, product(ascii_uppercase[:num], ['+', '', '-']))]

# printing result
print("Grades List : " + str(res))
