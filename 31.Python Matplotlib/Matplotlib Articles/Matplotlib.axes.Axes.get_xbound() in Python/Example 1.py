# Implementation of matplotlib function
from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt

fig, [ax, ax1] = plt.subplots(2, 1)
t = 4 * (np.random.rand(2, 100) - .5)
x = np.cos(2 * np.pi * t)
y = np.sin(2 * np.pi * t)

ax.plot(x, y, 'g')
lower, upper = ax.get_xbound()
ax.set_title('matplotlib.axes.Axes.get_xbound()\
Example\n Original Window',
             fontsize=14, fontweight='bold')

ax1.plot(x, y, 'g')
ax1.set_xbound(1.5 * lower, 0.5 * upper)
ax1.set_title('Window After Using get_xbound() function',
              fontsize=14, fontweight='bold')
plt.show()
