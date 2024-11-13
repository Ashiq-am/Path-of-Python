# importing modules
from matplotlib import pyplot
import numpy

# assign value to x axis
x_axis = numpy.arange(-2, 2, 0.1)

# get the value of sine
y_axis_sine = numpy.sin(x_axis)

# get the value of cos
y_axix_cose = numpy.cos(x_axis)

# create subplots using subplot() method
fig, axes = pyplot.subplots(2)

# depicting the visualization(scatter)
axes[0].scatter(x_axis, y_axis_sine, color='green', marker='*', label="sine")
axes[1].scatter(x_axis, y_axix_cose, color='blue', marker='*', label="cos")

# position at which legend to be added
axes[0].legend(loc='best')
axes[1].legend(loc='best')

# display the plot
pyplot.show()
