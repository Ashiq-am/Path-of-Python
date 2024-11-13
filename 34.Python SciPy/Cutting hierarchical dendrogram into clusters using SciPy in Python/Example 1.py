# Importing the libraries
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import dendrogram
import numpy as np
import matplotlib.pyplot as plt

# The data points are given as list of lists
data = np.array([
	[1, 4],
	[2, 2],
	[3, 7],
	[4, 6],
	[5, 1],
	[6, 3],
	[8, 10],
	[9, 11]
])

# Taking transpose
x, y = data.T

# plot our list in X,Y coordinates
plt.scatter(x, y)
plt.show()
