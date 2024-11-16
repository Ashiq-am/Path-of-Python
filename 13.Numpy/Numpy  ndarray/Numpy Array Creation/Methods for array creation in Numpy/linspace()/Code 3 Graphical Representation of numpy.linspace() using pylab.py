# Graphical Represenation of numpy.linspace()
import numpy as geek
import pylab as p

# Start = 0
# End = 2
# Samples to generate = 15
x1 = geek.linspace(0, 2, 15, endpoint = True)
y1 = geek.zeros(15)

p.plot(x1, y1, 'o')
p.xlim(-0.2, 2.1)
