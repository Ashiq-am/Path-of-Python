# Import libraries
import matplotlib
import numpy

# Create figure() objects
# This acts as a container
# for the different plots
fig = matplotlib.pyplot.figure()

# Generate line graph
x = numpy.arange(0, 1.414*2, 0.05)
y1 = numpy.sin(x)
y2 = numpy.cos(x)

# Creating two axes
# add_axes([xmin,ymin,dx,dy])
axes1 = fig.add_axes([0, 0, 1, 1])
axes1.plot(x, y1)
axes2 = fig.add_axes([0, 1, 1, 1])
axes2.plot(x, y2)

# Show plot
plt.show()
