# import primenu() method from sympy
from sympy.ntheory.factor_ import primenu

n = 2 * 3 * 7 * 11 * 13

# Use primenu() method
primenu_n = primenu(n)

print("Number of distinct prime factors of {} = {} ".format(n, primenu_n))
