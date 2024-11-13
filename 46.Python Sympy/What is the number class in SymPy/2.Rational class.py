# import Rational class from sympy
from sympy import Rational

# representing a rational number
print(Rational(1/2))

# Representing a string in p/q form
print(Rational("12/13"))

print(Rational(0.3))

# limiting the digits in denominator
print(Rational(0.3).limit_denominator(10))

# Passing 2 numbers as arguments to
# Rational class
print(Rational(5, 7))
