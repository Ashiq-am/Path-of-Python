# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, (axs, axs2) = plt.subplots(2, 1)
gs = axs2.get_gridspec()

axbig = fig.add_subplot(gs[1:, -1])
axbig.annotate("Second Axes", (0.4, 0.5),
               xycoords='axes fraction',
               va='center')

axs.set_title("Is artist is explicitly set transform : "
              + str(axs.is_transform_set()))

fig.suptitle('matplotlib.axes.Axes.is_transform_set() function Example', fontweight="bold")

plt.show()
