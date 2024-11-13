# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


verts = [(0., 0.), (0., 1.),
		(1., 1.), (1., 0.),
		(0., 0.)]

codes = [Path.MOVETO, Path.LINETO,
		Path.LINETO, Path.LINETO, Path.CLOSEPOLY]

path = Path(verts, codes)

fig, ax = plt.subplots()
patch = patches.PathPatch(path, facecolor ='green', lw = 2)
ax.add_patch(patch)
ax.set_xlim(-0.5, 2)
ax.set_ylim(-0.5, 2)

ax.text(0, 1.2,
		"Value Return : "+ str(path.contains_point([5, 5])),
		fontweight ="bold",
		fontsize = 10)

fig.suptitle('matplotlib.axes.Axes.contains_point()\
function Example', fontweight ="bold")

plt.show()
