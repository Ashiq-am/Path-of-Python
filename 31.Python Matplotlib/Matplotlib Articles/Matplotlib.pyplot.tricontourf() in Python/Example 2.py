# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

n_angles = 60
n_radii = 10
min_radius = 0.35
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (10 * radii * np.cos(angles)).flatten()
y = (10 * radii * np.sin(angles)).flatten()
z = (np.cos(4 * (radii) ** 2) * np.sin((angles) ** 2)).flatten()

triang = tri.Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)

tcf = plt.tricontourf(triang, z)

plt.colorbar(tcf)
plt.title('matplotlib.pyplot.tricontourf() Example\n',
          fontsize=14, fontweight='bold')

plt.show()
