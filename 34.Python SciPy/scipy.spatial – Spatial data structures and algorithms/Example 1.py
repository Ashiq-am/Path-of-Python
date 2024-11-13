from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt

points = np.array([[1, 4], [2, 1], [3, 0],
				[0, 2], [4, 3]])
tri = Delaunay(points)

plt.triplot(points[:, 0], points[:, 1], tri.simplices.copy())
plt.plot(points[:, 0], points[:, 1], 'o')
plt.show()
