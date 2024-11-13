# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np

# Create triangulation.
x = np.asarray([0, 1, 0, 3, 0.5, 1.5,
                2.5, 1, 2, 1.5])
y = np.asarray([0, 0, 0, 0, 1.0, 1.0,
                1.0, 2, 2, 3.0])

triangles = [[0, 1, 4], [1, 5, 4], [2, 6, 5],
             [4, 5, 7], [5, 6, 8], [5, 8, 7],
             [7, 8, 9], [1, 2, 5], [2, 3, 6]]

triang = mtri.Triangulation(x, y, triangles)
z = np.cos(2.5 * x * x) + np.sin(2.5 * x * x)

t = plt.tricontourf(triang, z)

plt.title('matplotlib.pyplot.tricontourf() Example\n',
          fontsize=14, fontweight='bold')

plt.show()
