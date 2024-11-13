# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt

fig, (axs, axs2) = plt.subplots(2, 1)
gs = axs2.get_gridspec()

# use of remove() method
Axis.remove(axs)

axbig = fig.add_subplot(gs[1:, -1])
axbig.annotate("Removed one Axes",
               (0.4, 0.5),
               xycoords='axes fraction',
               va='center')

fig.suptitle('matplotlib.axis.Axis.remove() \
function Example\n', fontweight="bold")

plt.show()
