# Python program explaining
# numpy.interp() function

# importing numpy as geek
import numpy as geek

x = [0, 1, 2.5, 2.72, 3.14]
xp = [2, 4, 6]
fp = [1, 3, 5]

gfg = geek.interp(x, xp, fp)

print(gfg)
