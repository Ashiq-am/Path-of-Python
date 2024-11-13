from scipy.spatial import ConvexHull
import numpy as np
import matplotlib.pyplot as plt

points = np.random.rand(10, 2)
hull = ConvexHull(points)

plt.plot(points[:, 0], points[:, 1], 'o')
for simplex in hull.simplices:
	plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

plt.show()
