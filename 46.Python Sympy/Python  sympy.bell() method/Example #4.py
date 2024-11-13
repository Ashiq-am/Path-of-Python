# import sympy
from sympy import *


n = 5
k = 3
variables = symbols('x:6')[1:]
print("Value of n = {}, k = {} and variables = {}".format(n, k, variables))

# Use sympy.bell() method
nth_bell_poly = bell(n, k, variables)

print("The nth bell polynomial of second kind : {}".format(nth_bell_poly))
