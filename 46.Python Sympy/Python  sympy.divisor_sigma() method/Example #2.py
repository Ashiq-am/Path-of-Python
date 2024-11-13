# import divisor_sigma() method from sympy
from sympy.ntheory import divisor_sigma

n = 15
k = 2

# Use divisor_sigma() method
divisor_sigma_n = divisor_sigma(n, k)

print("divisor_sigma({}, {}) = {} ".format(n, k, divisor_sigma_n))
# 1 ^ 2 + 3 ^ 2 + 5 ^ 2 + 15 ^ 2 = 260
