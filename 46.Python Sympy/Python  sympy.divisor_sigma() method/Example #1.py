# import divisor_sigma() method from sympy
from sympy.ntheory import divisor_sigma

n = 8

# Use divisor_sigma() method
divisor_sigma_n = divisor_sigma(n)

print("divisor_sigma({}) = {} ".format(n, divisor_sigma_n))
# 1 ^ 1 + 2 ^ 1 + 4 ^ 1 + 8 ^ 1 = 15
