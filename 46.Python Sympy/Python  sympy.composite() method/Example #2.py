# import sympy
from sympy import composite

n = 25

# Use composite() method
nth_composite = composite(n)

print("The {}th composite is {}".format(n, nth_composite))
