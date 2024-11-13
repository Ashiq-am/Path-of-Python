# importing sympy library
from sympy import *

# taking symbols
a, b = symbols('a b')

# calling find() method on expression
geek = (3 * a + b * log(a) + log(b) + log(a)*log(1 / b)).find(log)
print(geek)
