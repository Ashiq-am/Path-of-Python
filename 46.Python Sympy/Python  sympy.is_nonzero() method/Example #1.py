# Python program to check nonzero
# using sympy.is_nonzero() method

# importing sympy module
from sympy import *

# calling is_nonzero function on differnet numbers
geek1 = simplify(21).is_nonzero
geek2 = simplify(0).is_nonzero

print(geek1)
print(geek2)
