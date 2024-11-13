# import binomial_coefficients() method from sympy
from sympy.ntheory import binomial_coefficients

n = 6

# Use binomial_coefficients() method
binomial_coefficients_n = binomial_coefficients(n)

print("binomial_coefficients({}) = {} ".format(n, binomial_coefficients_n))
