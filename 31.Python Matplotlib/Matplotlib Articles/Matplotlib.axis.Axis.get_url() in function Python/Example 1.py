# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-40, 40, 0.5)
Y = np.arange(-40, 40, 0.5)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.plot(U, V)
ax.set_url('http://www.google.com')
fig.canvas.print_figure('scatter.svg')

ax.text(1.5, 5.5, "URL : "
        + str(Axis.get_url(ax)),
        fontweight="bold")

fig.suptitle('matplotlib.axis.Axis.get_url() \
function Example\n', fontweight="bold")

plt.show()
