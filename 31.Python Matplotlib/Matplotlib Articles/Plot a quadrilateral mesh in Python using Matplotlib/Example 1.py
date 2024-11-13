import matplotlib.pyplot as plt
import numpy as np


x1, y1 = 0.1, 0.05

# generate 2-D grids for the
# x & y bounds
y, x = np.mgrid[slice(-3, 3 + y1, y1), slice(-3, 4 + x1, x1)]
z = (1 - x / 2. + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

# Remove the last value from the
# z array as z must be inside x
# and y bounds.
z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

plt.subplot()

plt.pcolormesh(x, y, z,
			cmap ='YlGn',
			vmin = z_min,
			vmax = z_max,
			edgecolors = 'face',
			shading ='flat')

plt.title('pcolormesh_example')

# set the limits of the plot
# to the limits of the data
plt.axis([x.min(), x.max(), y.min(), y.max()])

plt.colorbar()
plt.show()
