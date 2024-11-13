# import antidivisor_count() method from sympy
from sympy.ntheory.factor_ import antidivisor_count

n = 128

# Use antidivisor_count() method
antidivisor_count_n = antidivisor_count(n)

print("The number of anti-divisors of {} : {}".format(n, antidivisor_count_n))
