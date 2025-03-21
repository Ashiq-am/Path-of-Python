# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np


ang = 40
rad = 10
radm = 0.35
radii = np.linspace(radm, 0.95, rad)

angles = np.linspace(0, np.pi, ang)
angles = np.repeat(angles[..., np.newaxis],
				rad, axis = 1)

angles[:, 1::2] += np.pi / ang

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
z = (np.sin(4 * radii) * np.cos(4 * angles)).flatten()

triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis = 1),
						y[triang.triangles].mean(axis = 1))
				< radm)

fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tpc = ax1.tripcolor(triang, z,
					shading ='flat')

fig1.colorbar(tpc)
ax1.set_title('matplotlib.pyplot.tripcolor() Example')
plt.show()
