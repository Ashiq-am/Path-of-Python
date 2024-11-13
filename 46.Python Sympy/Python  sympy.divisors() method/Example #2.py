# import divisors() method from sympy
from sympy import divisors

n = -210

# Use divisors() method
divisors_n = list(divisors(n, generator=True))

print("The divisors of {} : {}".format(n, divisors_n))
