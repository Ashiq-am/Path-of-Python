# importing sympy library
from sympy import *

# taking symbols
a, b = symbols('a b')

# calling count() method on expression
geek = (log(a * b**(1 - log(a)))).count(b)
print(geek)
