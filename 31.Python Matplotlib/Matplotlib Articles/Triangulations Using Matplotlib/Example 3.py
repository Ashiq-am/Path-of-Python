import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# A 2D array of points
points = np.array([[0, 0], [0, 1],
				[0, 2], [1, 0],
				[1, 1], [1, 2],
				[2, 0], [2, 1],
				[2, 2]])
# Perform Delaunay triangulation
tri = Delaunay(points)

# Visualize the triangulation
plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.show()
