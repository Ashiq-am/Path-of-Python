# Graphical Represenation of numpy.logspace()
import numpy as geek
import pylab as p

# Start = 0
# End = 2
# Samples to generate = 10
x1 = geek.logspace(0, 1, 10)
y1 = geek.zeros(10)

# Start = 0.1
# End = 1.5
# Samples to generate = 12
x2 = geek.logspace(0.1, 1.5, 12)
y2 = geek.zeros(12)

p.plot(x1, y1+0.05, 'o')
p.xlim(-0.2, 18)
p.ylim(-0.5, 1)
p.plot(x2, y2, 'x')
