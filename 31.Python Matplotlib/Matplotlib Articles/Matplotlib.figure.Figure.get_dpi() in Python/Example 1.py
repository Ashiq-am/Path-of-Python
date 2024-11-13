# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

fig = plt.figure(figsize=(5, 4))

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

xx = np.arange(0, 2 * np.pi, 0.01)
ax.plot(xx, np.sin(xx))

w = fig.get_dpi()
ax.text(1, 0, "Value Return by get_dpi() : "
        + str(w))

fig.canvas.draw()
fig.suptitle('matplotlib.figure.Figure.get_dpi() function \
Example', fontweight="bold")

plt.show()
