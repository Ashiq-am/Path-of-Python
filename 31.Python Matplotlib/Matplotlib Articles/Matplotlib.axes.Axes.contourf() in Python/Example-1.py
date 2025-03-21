# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
from numpy import ma
from matplotlib import ticker, cm

N = 1000
x = np.linspace(-6.0, 6.0, N)
y = np.linspace(-7.0, 7.0, N)
X, Y = np.meshgrid(x, y)

Z1 = np.exp(-(X)**2 - (Y)**2)
z = 50 * Z1
z[:5, :5] = -1
z = ma.masked_where(z <= 0, z)

fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator = ticker.LogLocator(),
				cmap ="Greens")

cbar = fig.colorbar(cs)
ax.set_title('matplotlib.axes.Axes.contourf() Example')

plt.show()
