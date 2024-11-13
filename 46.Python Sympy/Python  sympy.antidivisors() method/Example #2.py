# import antidivisors() method from sympy
from sympy.ntheory.factor_ import antidivisors

n = 128

# Use antidivisors() method
antidivisors_n = antidivisors(n)

print("The anti-divisors of {} : {}".format(n, antidivisors_n))
