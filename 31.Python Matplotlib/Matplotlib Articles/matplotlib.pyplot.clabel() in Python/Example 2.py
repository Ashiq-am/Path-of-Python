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
manual_locations = [(-1, -1.4), (-0.62, -0.7),
					(-2, 0.5), (1.7, 1.2),
					(2.0, 1.4), (2.4, 1.7)]

ax.clabel(CS, inline=1, fontsize=10, manual=manual_locations)
ax.set_title('labels at selected locations')
