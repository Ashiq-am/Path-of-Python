# Import sympy, P, Dice
from sympy.stats import P, Die

situation = Die('X', 6)

# Using stats.P() method
gfg = P(situation > 3)

print(gfg)
