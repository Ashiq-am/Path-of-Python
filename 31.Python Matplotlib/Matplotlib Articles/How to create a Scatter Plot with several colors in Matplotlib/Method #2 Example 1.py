# import required modules
import matplotlib.pyplot as plt
import numpy

# assign data points
a = numpy.array([[9, 1, 2, 7, 5, 8, 3, 4, 6],
				[4, 2, 3, 7, 9, 1, 6, 5, 8]])

# assign categories
categories = numpy.array([0, 1, 2, 0, 1, 2, 0, 1, 2])

# use colormap
colormap = numpy.array(['r', 'g', 'b'])

# depict illustration
plt.scatter(a[0], a[1], s=100, c=colormap[categories])
plt.show()
