# import divisors() method from sympy
from sympy import divisors

n = 84

# Use divisors() method
divisors_n = divisors(n)

print("The divisors of {} : {}".format(n, divisors_n))
