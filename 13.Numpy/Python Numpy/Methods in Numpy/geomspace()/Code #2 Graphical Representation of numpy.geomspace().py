# Graphical Represenation of numpy.geomspace()
import inline
import matplotlib
import numpy as geek
import pylab as p
matplotlib
inline

# Start = 1
# End = 3

# Samples to generate = 10
x1 = geek.geomspace(1, 3, 10, endpoint=False)
y1 = geek.ones(10)

p.plot(x1, y1, '+')
