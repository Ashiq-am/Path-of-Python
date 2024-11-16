# Python program explaining
# numpy.correlate() function

# importing numpy as geek
import numpy as geek

a = [2, 5, 7]
v = [0, 1, 0.5]

gfg = geek.correlate(a, v, "same")

print(gfg)
