# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x = np.arange(0, 10, 0.005)
y = np.exp(-x / 2.) * np.sin(2 * np.pi * x)

fig, [ax, ax1] = plt.subplots(1, 2)

ax.plot(x, y)
ax.set_title("Without get_yaxis_transform() function")

ax1.plot(x, y, transform = ax1.get_yaxis_transform())
ax1.set_title("With get_yaxis_transform() function")

fig.suptitle('matplotlib.axes.Axes.get_yaxis_transform() function Example', fontweight ="bold")

plt.show()
