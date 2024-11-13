# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

fig = plt.figure(edgecolor="red", figsize=(7, 6))

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

xx = np.arange(0, 2 * np.pi, 0.01)
ax.plot(xx, np.sin(xx))

w = fig.get_edgecolor()
ax.text(2, 0, "Value Return by get_edgecolor() :\n"
        + str(w),
        fontweight="bold")

fig.canvas.draw()
fig.suptitle('matplotlib.figure.Figure.get_edgecolor()\
function Example', fontweight="bold")

plt.show()
