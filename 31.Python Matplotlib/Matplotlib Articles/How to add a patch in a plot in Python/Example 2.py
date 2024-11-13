# import modules
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

Path = mpath.Path

# adjust figure and assign coordinates
fig, ax = plt.subplots()
pp = mpatches.PathPatch(Path([(0, 0), (10, 5), (10, 10), (20, 10)],
							[Path.MOVETO, Path.CURVE3,
							Path.CURVE3, Path.CLOSEPOLY]),
						transform=ax.transData)

# depict illustration
ax.add_patch(pp)
plt.show()
