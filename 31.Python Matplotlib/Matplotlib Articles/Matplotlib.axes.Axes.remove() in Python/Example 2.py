# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, (axs, axs2) = plt.subplots(2, 1)
gs = axs2.get_gridspec()

axs.remove()

axbig = fig.add_subplot(gs[1:, -1])
axbig.annotate("Removed one Axes",
               (0.4, 0.5),
               xycoords='axes fraction',
               va='center')

fig.suptitle('matplotlib.axes.Axes.remove() function Example', fontweight="bold")
plt.show()
