# import packages
from sympy.abc import x, y ,z

# creating an expression
expression = 4*x+5*y+6*z

# evaluating the expression
print(expression.evalf(3,subs={x:1,y:2,z:3}))
