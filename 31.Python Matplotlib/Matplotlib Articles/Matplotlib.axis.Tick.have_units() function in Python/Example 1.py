# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

delta = 15.0

angles = np.arange(0, 360 + delta, delta)
ells = [Ellipse((2, 2), 5, 2, a) for a in angles]

fig, ax = plt.subplots()

for e in ells:
    Tick.set_clip_box(e, ax.bbox)
    e.set_facecolor("green")
    e.set_alpha(0.05)
    ax.add_artist(e)

plt.xlim(-1, 5)
plt.ylim(-1, 5)

ax.set_title("Units are set on any axis : "
             + str(Tick.have_units(ax.xaxis)))

fig.suptitle('matplotlib.axis.Tick.have_units() \
function Example', fontweight="bold")

plt.show()
