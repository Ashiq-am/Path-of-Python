# importing SymPy Library
import sympy

# creating undefined function 'f'
f = sympy.Function('f')

# creating SymPy variable 'x'
x = sympy.Symbol('x')

# performing differentiation on the function 'f'
f(x).diff(x)
