from sympy import *

P, Q, R = symbols("P Q R")
expression = 3*P+6*Q-R

expanded_exp = expand(P*expression)
expanded_exp
