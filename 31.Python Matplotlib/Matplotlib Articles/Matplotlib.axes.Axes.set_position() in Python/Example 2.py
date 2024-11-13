# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

Z = np.random.rand(6, 30)

fig, (ax, ax1) = plt.subplots(1, 2)

ax.pcolor(Z)
ax1.pcolor(Z)

chartBox = ax1.get_position()
ax1.set_position([chartBox.x0,
				chartBox.y0,
				chartBox.width,
				chartBox.height * 0.6])

ax.set_title("Original Window")
ax1.set_title("Modified Window")

fig.suptitle('matplotlib.axes.Axes.set_position() function Example', fontweight ="bold")
plt.show()
