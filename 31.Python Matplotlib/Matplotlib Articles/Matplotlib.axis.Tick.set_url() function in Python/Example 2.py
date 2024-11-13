# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
delta = 0.025

x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)

Z1 = np.exp(-X ** 2 - Y ** 2)
Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
Z = (Z1 - Z2) * 2

im = ax.imshow(Z,
               interpolation='bilinear',
               cmap="bone",
               origin='lower',
               extent=[-3, 3, -3, 3])

Tick.set_url(im, 'http://www.google.com')
fig.canvas.print_figure('geeks2.svg')

fig.suptitle('matplotlib.axis.Tick.set_url() \
function Example', fontweight="bold")

plt.show()
