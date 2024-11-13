# Implementation of matplotlib function
from matplotlib.artist import Artist
import numpy as np
import matplotlib.pyplot as plt

X = np.random.rand(10, 200)
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(xs, ys, 'go-', picker=5)

ax.set_picker(True)

ax.text(0.48, 0.3, "Value return : "
        + str(Artist.get_picker(ax)),
        fontweight="bold",
        fontsize=18)

fig.suptitle('matplotlib.artist.Artist.get_picker() \
function Example', fontweight="bold")

plt.show()
