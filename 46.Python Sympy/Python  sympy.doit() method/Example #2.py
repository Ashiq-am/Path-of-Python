# importing sympy library
from sympy import *

# taking symbols
a, b = symbols('a b')

# calling doit() method on expression
geek = (3 * a + b * log(a) + log(b) + log(a)*log(1 / b)).doit()
print(geek)
