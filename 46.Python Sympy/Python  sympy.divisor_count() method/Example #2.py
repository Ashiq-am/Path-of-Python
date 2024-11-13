# import divisor_count() method from sympy
from sympy import divisor_count

n = 12

# Use divisor_count() method
divisor_count_n = divisor_count(n, modulus=2)

print("The number of divisors of {} : {}".format(n, divisor_count_n))
