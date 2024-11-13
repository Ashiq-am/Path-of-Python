# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt


fig, ax4 = plt.subplots()

x = 10.0**np.linspace(0.0, 2.0, 15)
y = x**2.0
ax4.set_xscale("log", nonposx ='clip')
ax4.set_yscale("log", nonposy ='clip')

ax4.errorbar(x, y, xerr = 0.1 * x,
			yerr = 2.0 + 1.75 * y,
			color ="green")

ax4.set_ylim(bottom = 0.1)

fig.suptitle('matplotlib.axes.Axes.set_yscale() function Example\n', fontweight ="bold")

plt.show()
