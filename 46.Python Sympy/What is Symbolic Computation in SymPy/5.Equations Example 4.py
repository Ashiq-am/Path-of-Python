from sympy import *

P = Symbol("P")
expression = (P**2+3*P-4)/3
# P^2+3P-4

solve(expression, P)
