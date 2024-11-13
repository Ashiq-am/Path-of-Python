# importing sympy library
from sympy import *

# taking symbols
a, b = symbols('a b')

# calling count() method on expression
geek = (log(a) + log(b) + log(a)*log(1 / b)).count(b)
print(geek)
