# importing Matplotlib and Numpy Packages
import numpy as np
import matplotlib.pyplot as plt

# The data are given as list of lists (2d list)
data = np.array([
	[1, 4],
	[2, 2],
	[3, 7],
	[4, 6],
	[5, 0],
	[6, 3]
])
# Taking transpose
x, y = data.T


# plot our list in X,Y coordinates
plt.scatter(x, y)
plt.show()
