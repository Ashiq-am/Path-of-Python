# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.tri as tri

dx, dy = 0.015, 0.05
x = np.arange(-4.0, 4.0, dx)
y = np.arange(-4.0, 4.0, dy)
X, Y = np.meshgrid(x, y)

extent = np.min(x), np.max(x), np.min(y), np.max(y)

Z1 = np.add.outer(range(8), range(8)) % 2
plt.imshow(Z1, cmap="binary_r",
           interpolation='nearest',
           extent=extent,
           alpha=1)


def geeks(x, y):
    return (1 - x / 2 + x ** 5 + y ** 6) * np.exp(-(x ** 2 + y ** 2))


Z2 = geeks(X, Y)

x = plt.imshow(Z2, cmap="Greens",
               alpha=0.7,
               interpolation='bilinear',
               extent=extent)
plt.close(1)
ang = 40
rad = 10
radm = 0.35
radii = np.linspace(radm, 0.95, rad)

angles = np.linspace(0, 0.5 * np.pi, ang)
angles = np.repeat(angles[...,
                          np.newaxis],
                   rad, axis=1)

angles[:, 1::2] += np.pi / ang

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
z = (np.sin(4 * radii) * np.cos(4 * angles)).flatten()

triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < radm)

tpc = plt.tripcolor(triang, z,
                    shading='flat')

plt.colorbar(tpc)
plt.plasma()

plt.title('matplotlib.pyplot.close() Example')
plt.show()
