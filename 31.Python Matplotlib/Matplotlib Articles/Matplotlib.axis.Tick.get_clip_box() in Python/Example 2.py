# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

NUM = 100

ells = [Ellipse(xy=np.random.rand(2) * 10,
				width=np.random.rand()*2,
				height=np.random.rand()*2,
				angle=np.random.rand() * 360)
		for i in range(NUM)]

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

print("Value Return by get_clip_box()")
x = 0

for e in ells:
	ax.add_artist(e)
	e.set_clip_box(ax.bbox)
	e.set_alpha(np.random.rand())
	e.set_facecolor(np.random.rand(4))

	if x < 3:
		print(Tick.get_clip_box(e))
		x += 1

ax.set_xlim(3, 7)
ax.set_ylim(3, 7)

fig.suptitle("""matplotlib.axis.Tick.get_clip_box()
function Example\n""", fontweight="bold")

plt.show()
