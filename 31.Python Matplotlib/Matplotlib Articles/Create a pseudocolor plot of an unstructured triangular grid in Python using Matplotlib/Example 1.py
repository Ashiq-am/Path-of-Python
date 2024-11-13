import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
import math

# Creating a Triangulation without
# specifying the triangles results in the
# Delaunay triangulation of the points.

# First create the x and y coordinates of the points.
angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles1 = np.linspace(0, 2 * math.pi, angles, endpoint = False)
angles1 = np.repeat(angles1[..., np.newaxis], n_radii, axis = 1)
angles1[:, 1::2] += math.pi / angles

x = (radii * np.cos(angles1)).flatten()
y = (radii * np.sin(angles1)).flatten()
z = (np.cos(radii)*np.cos(angles1 * 3.0)).flatten()

# Create Delaunay triangulation.
triang = tri.Triangulation(x, y)

# Mask off unwanted triangles.
x1 = x[triang.triangles].mean(axis = 1)
y1 = y[triang.triangles].mean(axis = 1)
mask = np.where(x1 * x1 + y1 * y1 < min_radius * min_radius, 1, 0)
triang.set_mask(mask)

# Illustrate shading.
plt.figure()
plt.gca().set_aspect('equal')

tri = plt.tripcolor(triang, z,
					shading ='gouraud',
					cmap = plt.cm.rainbow,
					alpha = 0.5,
					edgecolors ='k')

plt.title('tripcolor_example1')
plt.colorbar(tri)
