# Python program to check positive number
# using sympy.is_positive() method

# importing sympy module
from sympy import *

# calling is_positive function on differnet numbers
geek1 = simplify(-21).is_positive
geek2 = simplify(0).is_positive

print(geek1)
print(geek2)
