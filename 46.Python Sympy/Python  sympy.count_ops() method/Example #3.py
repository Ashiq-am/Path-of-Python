# importing sympy library
from sympy import *

# taking symbols
a, b = symbols('a b')

# calling count_ops() method on expression
geek = log(a * b**(1 - log(a)))
print(count_ops(geek))
