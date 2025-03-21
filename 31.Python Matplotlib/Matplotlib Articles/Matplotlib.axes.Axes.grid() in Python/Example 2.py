# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
y1 = -3 * x * x + 10 * x + 10
y2 = 3 * x * x + x

fig, [ax, ax1] = plt.subplots(2, 1,
                              sharex=True)

ax.plot(x, y1, x, y2, color='black')
ax.fill_between(x, y1, y2, where=y2 > y1,
                facecolor='green',
                alpha=0.8)

ax.fill_between(x, y1, y2, where=y2 <= y1,
                facecolor='black',
                alpha=0.8)

ax.xaxis.grid(True, color="black")
ax.set_title('matplotlib.axes.Axes.grid() \
Example\n\n Grid in X-axis',
             fontsize=12, fontweight='bold')

ax1.plot(x, y1, x, y2, color='black')
ax1.fill_between(x, y1, y2, where=y2 > y1,
                 facecolor='green',
                 alpha=0.8)

ax1.fill_between(x, y1, y2, where=y2 <= y1,
                 facecolor='black',
                 alpha=0.8)

ax1.yaxis.grid(True, color="black")
ax1.set_title('Grid in y-axis',
              fontsize=12, fontweight='bold')
plt.show()
