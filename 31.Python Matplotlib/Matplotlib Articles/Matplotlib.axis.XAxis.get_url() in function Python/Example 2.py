# Implementation of matplotlib function
from matplotlib.axis import XAxis
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
delta = 0.25

x = y = np.arange(-4.0, 5.0, delta)
X, Y = np.meshgrid(x, y)

Z1 = np.exp(-X ** 2 - Y ** 2)
Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
Z = (Z1 - Z2) * 2

ax.imshow(Z, interpolation='bilinear',
          cmap="BuGn",
          origin='lower',
          extent=[-3, 3, -3, 3])

ax.set_url('https://www.geeksforgeeks.org/')
ax.set_title("URL : " + str(XAxis.get_url(ax)),
             fontweight="bold")

fig.suptitle('matplotlib.axis.XAxis.get_url() \
function Example\n', fontweight="bold")

plt.show()
