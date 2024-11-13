from sympy import *

x = Symbol('x')

print(trigsimp(cos(x)/sin(x)))
print(trigsimp(sin(x)**2+cos(x)**2))
