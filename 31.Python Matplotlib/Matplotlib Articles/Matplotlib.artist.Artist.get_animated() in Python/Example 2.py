# Implementation of matplotlib function
from matplotlib.artist import Artist
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

L = 50
theta = np.linspace(0, 2 * np.pi, L)
r = np.ones_like(theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

line, = ax.plot(1, 0, 'ro')

annotation = ax.annotate(
    'annotation', xy=(1, 0), xytext=(-1, 0),
    arrowprops={'arrowstyle': "->"}
)
Artist.set_animated(annotation, False)
w = Artist.get_animated(annotation)

print(str(w))

fig.suptitle('matplotlib.artist.Artist.get_animated()\
function Example', fontweight="bold")

ax.grid()

plt.show()
