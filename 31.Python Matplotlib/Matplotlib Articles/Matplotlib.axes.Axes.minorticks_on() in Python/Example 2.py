# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 1.2 * np.sin(4 * np.pi * x)

fig, (ax, ax1) = plt.subplots(1, 2)

ax.fill_between(x, y1, y2, color ="green",
				alpha = 0.6)
ax.set_title("Without minorticks_on()")

ax1.fill_between(x, y1, y2, color ="green",
				alpha = 0.6)
ax1.minorticks_on()
ax1.set_title("With minorticks_on()")

fig.suptitle('matplotlib.axes.Axes.minorticks_on() function Example\n\n', fontweight ="bold")
plt.show()
