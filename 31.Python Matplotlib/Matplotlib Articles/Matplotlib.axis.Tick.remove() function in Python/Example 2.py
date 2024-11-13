# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt

fig, (axs, axs2) = plt.subplots(1, 2)
gs = axs2.get_gridspec()

# use of remove() method
Tick.remove(axs)

axbig = fig.add_subplot(gs[0:, -1])
axbig.annotate("Removed one Axes",
               (0.4, 0.5),
               xycoords='axes fraction',
               va='center')

fig.suptitle('matplotlib.axis.Tick.remove() \
function Example', fontweight="bold")

plt.show()
