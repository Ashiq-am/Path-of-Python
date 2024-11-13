# importing modules
from matplotlib import pyplot
import numpy

# assign value to x axis
x_axis = numpy.arange(1, 20, 0.5)

# get the value of log10
y_axis_log10 = numpy.log10(x_axis)

# get the value of exp
y_axix_exp = numpy.exp(x_axis)

# create subplots using subplot() method
fig, axes = pyplot.subplots(2)

# depicting the visualization
axes[0].plot(x_axis, y_axis_log10, color='green', label="log10")
axes[1].plot(x_axis, y_axix_exp, color='blue', label="exp")

# position at which legend to be added
axes[0].legend(loc='best')
axes[1].legend(loc='best')

# display the plot
pyplot.show()
