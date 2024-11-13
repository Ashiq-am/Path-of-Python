# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

NUM = 20

ells = [Ellipse(xy=np.random.rand(2) * 10,
				width=np.random.rand()*4,
				height=np.random.rand()*4,
				angle=np.random.rand() * 360)
		for i in range(NUM)]

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

print("Last 10 child Artists of this Artist \n")
for e in ells:
	ax.add_artist(e)
	e.set_clip_box(ax.bbox)
	e.set_alpha(np.random.rand())
	e.set_facecolor(np.random.rand(4))

print(*list(ax.get_children())[-10:], sep="\n")

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

fig.suptitle("""matplotlib.axis.Tick.get_children()
function Example\n""", fontweight="bold")

plt.show()
