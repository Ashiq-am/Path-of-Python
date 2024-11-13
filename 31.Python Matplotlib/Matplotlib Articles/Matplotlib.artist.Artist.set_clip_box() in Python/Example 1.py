# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

delta = 45.0

angles = np.arange(0, 360 + delta, delta)
ells = [Ellipse((2, 2), 5, 2, a) for a in angles]

fig, ax = plt.subplots()

for e in ells:
    Artist.set_clip_box(e, ax.bbox)
    e.set_alpha(0.1)
    ax.add_artist(e)

plt.xlim(-1, 5)
plt.ylim(-1, 5)

fig.suptitle('matplotlib.artist.Artist.set_clip_box() \
function Example', fontweight="bold")

plt.show()
