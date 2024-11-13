# Python program to check non-positive number
# using sympy.is_nonpositive() method

# importing sympy module
from sympy import *

# calling is_nonpositive function on differnet numbers
geek1 = simplify(-21).is_nonpositive
geek2 = simplify(0).is_nonpositive

print(geek1)
print(geek2)
