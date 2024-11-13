# Import sympy, P, Dice
from sympy.stats import P, Die

situation = Die('X', 2)

# Using stats.P() method
gfg = P(situation < 5)

print(gfg)
