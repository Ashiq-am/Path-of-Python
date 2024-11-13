# Python program to check negative number
# using sympy.is_negative() method

# importing sympy module
from sympy import *

# calling is_negative function on differnet numbers
geek1 = simplify(-21).is_negative
geek2 = simplify(0).is_negative

print(geek1)
print(geek2)
