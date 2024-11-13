# importing SymPy Library
import sympy

# creating a SymPy variable 'x'
x = sympy.Symbol('x')

#creating another SymPy variable 'y'
y = sympy.Symbol('y')

# creating non-callable function
f = sympy.Function('f')(x)

# calling the function 'f' with an argument
f(y)
