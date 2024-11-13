# importing the required libraries
import numpy
import matplotlib.pyplot

# creating the graph
delta = 0.025
x = numpy.arange(-3.0, 3.0, delta)
y = numpy.arange(-2.0, 2.0, delta)
X, Y = numpy.meshgrid(x, y)

Z1 = numpy.exp(-X**2 - Y**2)
Z2 = numpy.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

# adding labels to the line contours
fig, ax = matplotlib.pyplot.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('Simplest default with labels')
