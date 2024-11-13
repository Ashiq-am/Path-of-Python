# import binomial_coefficients_list() method from sympy
from sympy.ntheory import binomial_coefficients_list

n = 9

# Use binomial_coefficients_list() method
binomial_coefficients_list_n = binomial_coefficients_list(n)

print("{}th row of Pascal's Triangle = {} ".format(n, binomial_coefficients_list_n))
