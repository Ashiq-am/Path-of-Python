# import udivisors() method from sympy
from sympy.ntheory.factor_ import udivisors

n = -210

# Use udivisors() method
udivisors_n = list(udivisors(n, generator=True))

print("The unitary divisors of {} : {}".format(n, udivisors_n))
