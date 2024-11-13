from sympy import *

P, Q, R = symbols("P Q R")
expression = 3*P+6*Q-R
# 3P+6Q-R

expanded_exp = expand(P*expression)
# 3P^2+6PQ-PR

factor(expanded_exp)
