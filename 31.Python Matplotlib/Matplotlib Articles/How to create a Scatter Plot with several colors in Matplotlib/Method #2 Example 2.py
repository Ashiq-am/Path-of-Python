# import required modules
import matplotlib.pyplot as plt
import numpy

# assign data points
a = numpy.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
				[9, 8, 7, 6, 5, 4, 3, 2, 1]])

# assign categories
categories = numpy.array([0, 1, 1, 0, 0, 1, 1, 0, 1])

# assign colors using color codes
color1 = (0.69411766529083252, 0.3490196168422699,
		0.15686275064945221, 1.0)
color2 = (0.65098041296005249, 0.80784314870834351,
		0.89019608497619629, 1.0)

# asssign colormap
colormap = numpy.array([color1, color2])

# depict illustration
plt.scatter(a[0], a[1], s=500, c=colormap[categories])
plt.show()
