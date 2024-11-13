# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, ax = plt.subplots()

ax.pcolor(xx)
ax.set_zorder(-20)

ax.set_title("Zorder Value : "
             + str(ax.get_zorder()))

fig.suptitle('matplotlib.axes.Axes.get_zorder() \
function Example', fontweight="bold")

plt.show()
