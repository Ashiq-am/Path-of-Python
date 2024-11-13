import matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(3, 4,
                         sharex='row',
                         sharey='row',
                         squeeze=False)

data = np.random.rand(20, 2, 10)

for ax in axes.flatten()[:-1]:
    ax.plot(*np.random.randn(2, 10), marker="o", ls="")

# Now remove axes[1, 5] from
# the grouper for xaxis
axes[2, 3].get_shared_x_axes().remove(axes[2, 3])

# Create and assign new ticker
xticker = matplotlib.axis.Ticker()
axes[2, 3].xaxis.major = xticker

# The new ticker needs new locator
# and formatters
xloc = matplotlib.ticker.AutoLocator()
xfmt = matplotlib.ticker.ScalarFormatter()

axes[2, 3].xaxis.set_major_locator(xloc)
axes[2, 3].xaxis.set_major_formatter(xfmt)

# Now plot to the "ungrouped" axes
axes[2, 3].plot(np.random.randn(10) * 100 + 100,
                np.linspace(-3, 3, 10),
                marker="o", ls="",
                color="green")

plt.show()
