# import required modules
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# create objects
fig, axes = plt.subplots(ncols=3, nrows=3,)
gs = axes[1, 2].get_gridspec()

# create sub plots as grid
for ax in axes[1:, -1]:
	ax.remove()
axsbig = fig.add_subplot(gs[1:, -1])
axsbig.annotate('Big Axes \nGridSpec[1:, -1]',
				(0.1, 0.5),
				xycoords='axes fraction',
				va='center', color="g")

# depict illustartion
fig.tight_layout()
plt.show()
