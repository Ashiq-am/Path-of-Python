# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

n_angles = 24
n_radii = 9
min_radius = 0.5
radii = np.linspace(min_radius, 0.9, n_radii)

angles = np.linspace(0, np.pi, n_angles, endpoint = False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis = 1)
angles[:, 1::2] += np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
triang = tri.Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis = 1),
						y[triang.triangles].mean(axis = 1))
				< min_radius)

fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
ax1.triplot(triang, 'go-', lw = 2)
ax1.set_title('matplotlib.axes.Axes.triplot() Example')
plt.show()
