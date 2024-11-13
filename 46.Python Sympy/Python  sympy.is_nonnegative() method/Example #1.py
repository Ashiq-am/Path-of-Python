# Python program to check nonnegative number
# using sympy.is_nonnegative() method

# importing sympy module
from sympy import *

# calling is_nonnegative function on differnet numbers
geek1 = simplify(-21).is_nonnegative
geek2 = simplify(0).is_nonnegative

print(geek1)
print(geek2)
