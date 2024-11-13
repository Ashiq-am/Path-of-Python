# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

Z = np.random.rand(6, 30)

fig, ax1 = plt.subplots()

ax1.pcolor(Z)

chartBox = ax1.get_position()
x, y, x1, y1 = chartBox.x0, chartBox.y0, chartBox.x1, chartBox.y1

ax1.text(4, 6.35, "Bbox - xmin : "+str(x),
		fontweight ="bold")
ax1.text(19, 6.35, "Bbox - ymin : "+str(round(y, 2)),
		fontweight ="bold")
ax1.text(4, 6.15, "Bbox - xmax : "+str(x1),
		fontweight ="bold")
ax1.text(19, 6.15, "Bbox - ymax : "+str(y1),
		fontweight ="bold")
fig.suptitle('matplotlib.axes.Axes.get_position() function Example\n', fontweight ="bold")
plt.show()
