# import required modules
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# create objects
fig = plt.figure()
gridspan = fig.add_gridspec(2, 2)

# create sub plots as grid
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[:, -1])

# depict illustartion
plt.show()
