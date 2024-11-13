# import required modules
import numpy
from matplotlib import pyplot
import matplotlib

# assign value to x axis
x_axis = numpy.arange(1, 20, 0.5)

# get the value of log10
y_axis_log10 = numpy.exp(x_axis)

# plot the graph
pyplot.plot(x_axis, y_axis_log10, c="blue", label="exponential")

# Title of the graph/ploy
pyplot.title("Exponential Graph Plot")

# to set the font size of the legend
matplotlib.rcParams['legend.fontsize'] = 25

pyplot.legend(loc='best')

pyplot.show()
