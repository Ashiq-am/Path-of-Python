# importing SymPy Library
import sympy

# creating a SymPy variable 'x'
x = sympy.Symbol('x')

# creating non-callable function
f = sympy.Function('f')(x)

# calling the function 'f'
f
