# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import numpy as np

rx, ry = 3., 1.

value1 = rx * ry * np.pi
value2 = np.arange(0, 3 * np.pi + 0.01, 0.2)
value3 = np.column_stack([rx / value1 * np.cos(value2),
                          ry / value1 * np.sin(value2)])

x, y, s, c = np.random.rand(4, 99)
s *= 10 ** 2.

fig, ax = plt.subplots()
ax.scatter(x, y, s, c, marker=value3)

Artist.set_alpha(ax, 0.5)

w = Artist.get_alpha(ax)
ax.set_title("Alpha Value : " + str(w))

fig.suptitle('matplotlib.artist.Artist.get_alpha()\
function Example', fontweight="bold")

plt.show()
