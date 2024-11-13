# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.artist import Artist

np.random.seed(10 ** 7)
geeksx = np.random.randn(10)

fig, ax = plt.subplots()
ax.plot(geeksx)

ax.text(1.5, 0.85,
        "Value return by format_cursor_data():",
        fontweight="bold")

ax.text(0, 0.7,
        Artist.format_cursor_data(ax, data=geeksx))

fig.suptitle('matplotlib.artist.Artist.format_cursor_data()\
function Example', fontweight="bold")

plt.show()
