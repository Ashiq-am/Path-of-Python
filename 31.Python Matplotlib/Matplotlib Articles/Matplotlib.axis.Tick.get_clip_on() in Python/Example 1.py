# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse


delta = 10.0

angles = np.arange(0, 360 + delta, delta)
ells = [Ellipse((2, 2), 5, 2, a) for a in angles]

fig, ax = plt.subplots()

for e in ells:
	e.set_alpha(0.1)
	ax.add_artist(e)

ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)

print("Value Return by get_clip_on() : ",
	Tick.get_clip_on(ax))

fig.suptitle("""matplotlib.axis.Tick.get_clip_on()
function Example\n""", fontweight="bold")

plt.show()
