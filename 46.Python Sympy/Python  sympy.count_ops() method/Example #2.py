# importing sympy library
from sympy import *

# taking symbols
a, b = symbols('a b')

# calling count_ops() method on expression
geek = log(a) + log(b) + log(a)*log(1 / b)
print(count_ops(geek))
