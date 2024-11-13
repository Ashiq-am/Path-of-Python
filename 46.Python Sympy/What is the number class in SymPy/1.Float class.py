# import Float class from sympy
from sympy import Float

# converting integer to float
print(Float(5))

# limiting the digits
print(Float(22.7))
print(Float(22.7, 4))

# Scientific notation to number format
print(Float('99.99E1'))
