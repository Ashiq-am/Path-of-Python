# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
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

Axis.set_url(im, 'http://www.google.com')
fig.canvas.print_figure('geeks2.svg')

fig.suptitle('matplotlib.axis.Axis.set_url() \
function Example\n', fontweight="bold")

plt.show()
