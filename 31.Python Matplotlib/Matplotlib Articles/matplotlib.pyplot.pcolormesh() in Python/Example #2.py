# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

dx, dy = 0.015, 0.05
y, x = np.mgrid[slice(-4, 4 + dy, dy),
                slice(-4, 4 + dx, dx)]
z = (1 - x / 3. + x ** 6 + y ** 3) * np.exp(-x ** 2 - y ** 2)
z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

c = plt.pcolormesh(x, y, z, cmap='Greens', vmin=z_min, vmax=z_max)
plt.colorbar(c)

plt.title('matplotlib.pyplot.pcolormesh() function Example', fontweight="bold")
plt.show()
