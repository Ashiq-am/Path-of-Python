# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-10, 10, 0.5)
Y = np.arange(-10, 10, 0.5)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.scatter(U, V)
ax.set_url('http://www.google.com')
fig.canvas.print_figure('Geeks.svg')

ax.text(-5, 10.5, "URL : "
        + str(Tick.get_url(ax)),
        fontweight="bold")

fig.suptitle('matplotlib.axis.Tick.get_url() \
function Example\n', fontweight="bold")

plt.show()
