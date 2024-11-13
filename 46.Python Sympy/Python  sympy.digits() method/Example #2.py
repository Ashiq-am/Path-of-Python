# import digits() method from sympy
from sympy.ntheory.factor_ import digits

n = 33
b = 2

# Use digits() method
digits_n_b = digits(n, b)

print("Digits of {} in base {} = {} ".format(n, b, digits_n_b))