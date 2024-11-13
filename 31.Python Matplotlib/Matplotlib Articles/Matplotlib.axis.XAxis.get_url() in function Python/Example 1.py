# Implementation of matplotlib function
from matplotlib.axis import XAxis
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-60, 55, 0.4)
Y = np.arange(-60, 40, 0.4)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.plot(U, V)
ax.set_url('http://www.google.com')
fig.canvas.print_figure('scatter.svg')

ax.text(1.5, 5.5, "URL : "
        + str(XAxis.get_url(ax)),
        fontweight="bold")

fig.suptitle('matplotlib.axis.XAxis.get_url() function\
Example\n', fontweight="bold")

plt.show()
