# importing the required libraries
import numpy
import matplotlib.pyplot

# creating the graph
from plotly.figure_factory._violin import np

delta = 0.025
x = numpy.arange(-3.0, 3.0, delta)
y = numpy.arange(-2.0, 2.0, delta)
X, Y = numpy.meshgrid(x, y)

Z1 = numpy.exp(-X**2 - Y**2)
Z2 = numpy.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

# adding labels to the line contours
fig, ax = matplotlib.pyplot.subplots()
CS = ax.contour(X, Y, Z, 6,
				linewidths = np.arange(.5, 4, .5),
				colors=('r', 'green', 'blue',
						(1, 1, 0), '#afeeee', '0.5')
				)

ax.clabel(CS, fontsize=9, inline=1)
ax.set_title('Crazy lines')
