# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt

fig, (axs, axs2) = plt.subplots(2, 1)
gs = axs2.get_gridspec()

axbig = fig.add_subplot(gs[1:, -1])
axbig.annotate("Second Axes", (0.5, 0.6),
               xycoords='axes fraction',
               va='center')

axs.set_title("Is artist is explicitly set transform : "
              + str(Axis.is_transform_set(axs)))

fig.suptitle('matplotlib.axis.Axis.is_transform_set() \
function Example\n', fontweight="bold")

plt.show()
