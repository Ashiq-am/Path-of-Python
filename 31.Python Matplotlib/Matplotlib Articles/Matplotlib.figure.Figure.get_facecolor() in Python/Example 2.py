# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

fig = plt.figure(facecolor="red", figsize=(7, 6))

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

xx = np.arange(0, 2 * np.pi, 0.01)
ax.plot(xx, np.sin(xx))

w = fig.get_facecolor()
ax.text(2, 0,
        "Value Return by get_facecolor() :\n"
        + str(w),
        fontweight="bold")

fig.canvas.draw()

fig.suptitle('matplotlib.figure.Figure.get_facecolor()\
function Example', fontweight="bold")

plt.show()
