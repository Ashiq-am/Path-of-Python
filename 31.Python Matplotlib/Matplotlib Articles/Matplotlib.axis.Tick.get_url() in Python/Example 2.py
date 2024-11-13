# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
delta = 0.025

x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)

Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

ax.imshow(Z, interpolation='bilinear',
		cmap="inferno",
		origin='lower',
		extent=[-3, 3, -3, 3])

ax.set_url('https://www.geeksforgeeks.org/')
ax.set_title("URL : "+str(Tick.get_url(ax)),
			fontweight="bold")

fig.suptitle('matplotlib.axis.Tick.get_url() \
function Example\n', fontweight="bold")

plt.show()
