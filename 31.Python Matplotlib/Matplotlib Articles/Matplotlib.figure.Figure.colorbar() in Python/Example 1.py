# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np

# Create triangulation.
x = np.asarray([0, 1, 2, 3, 0.5,
                1.5, 2.5, 1, 2,
                1.5])

y = np.asarray([0, 0, 0, 0, 1.0,
                1.0, 1.0, 2, 2,
                3.0])

triangles = [[0, 1, 4], [1, 5, 4],
             [2, 6, 5], [4, 5, 7],
             [5, 6, 8], [5, 8, 7],
             [7, 8, 9], [1, 2, 5],
             [2, 3, 6]]

triang = mtri.Triangulation(x, y, triangles)
z = np.cos(3 * x) * np.cos(6 * y) + np.sin(6 * x)

fig, axs = plt.subplots()
t = axs.tricontourf(triang, z)
axs.tricontour(triang, z, colors='white')
fig.colorbar(t)

fig.suptitle('matplotlib.figure.Figure.colorbar() \
function Example\n\n', fontweight="bold")

plt.show()
