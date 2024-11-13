# Demonstration of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

N = 100
X, Y = np.mgrid[-4:4:complex(0, N), -4:4:complex(0, N)]

# Image show that a low hump with a spike coming out.
# We need a z/colour axis on a log scale in order
# to watch both hump and spike.
Z1 = np.exp(-(X)**2 - (Y)**2)
Z2 = np.exp(-(X * 10)**2 - (Y * 10)**2)
Z = Z1 + 50 * Z2

fig, (ax0, ax1) = plt.subplots(2, 1)

c = ax0.pcolor(X, Y, Z,norm=LogNorm(vmin=Z.min(), vmax=Z.max()), cmap=plt.cm.autumn)

fig.colorbar(c, ax=ax0)

c = ax1.pcolor(X, Y, Z, cmap=plt.cm.autumn)
fig.colorbar(c, ax=ax1)

plt.show()
