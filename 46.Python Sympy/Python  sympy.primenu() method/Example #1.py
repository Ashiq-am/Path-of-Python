# import primenu() method from sympy
from sympy.ntheory.factor_ import primenu

n = 24

# Use primenu() method
primenu_n = primenu(n)

print("Number of distinct prime factors of {} = {} ".format(n, primenu_n))  # 2 and 3
