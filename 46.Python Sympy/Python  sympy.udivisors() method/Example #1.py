# import udivisors() method from sympy
from sympy.ntheory.factor_ import udivisors

n = 84

# Use udivisors() method
udivisors_n = udivisors(n)

print("The unitary divisors of {} : {}".format(n, udivisors_n))
