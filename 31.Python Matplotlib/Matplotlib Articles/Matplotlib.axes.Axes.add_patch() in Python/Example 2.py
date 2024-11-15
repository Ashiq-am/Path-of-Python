# Implementation of matplotlib function
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

Path = mpath.Path

fig, ax = plt.subplots()
pp1 = mpatches.PathPatch(
	Path([(0, 0), (1, 0), (1, 1), (0, 0)],
		[Path.MOVETO, Path.CURVE3,
		Path.CURVE3, Path.CLOSEPOLY]),
	fc ="none", transform = ax.transData)

ax.add_patch(pp1)
ax.plot([0.75], [0.25], "go-")

fig.suptitle('matplotlib.axes.Axes.add_patch() function Example\n\n', fontweight ="bold")
plt.show()
