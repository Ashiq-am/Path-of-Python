# import divisor_count() method from sympy
from sympy.ntheory.factor_ import udivisor_count

n = 210

# Use udivisor_count() method
udivisor_count_n = udivisor_count(n)

print("The unitary number of divisors of {} : {}".format(n, udivisor_count_n))
