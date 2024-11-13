# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

n_angles = 26
n_radii = 10
min_radius = 0.35
radii = np.linspace(min_radius,
                    0.95, n_radii)

angles = np.linspace(0, 3 * np.pi,
                     n_angles,
                     endpoint=False)

angles = np.repeat(angles[..., np.newaxis],
                   n_radii, axis=1)

angles[:, 1::2] += np.pi / n_angles

x = (10 * radii * np.cos(angles)).flatten()
y = (10 * radii * np.sin(angles)).flatten()
z = (np.cos(16 * radii) * np.cos(3 * angles) + np.sin(8 * radii)).flatten()

triang = tri.Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)

fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tcf = ax1.tricontourf(triang, z)
fig1.colorbar(tcf)
ax1.tricontour(triang, z, colors='k')
fig1.suptitle('matplotlib.pyplot.tricontour() Example')

plt.show()
