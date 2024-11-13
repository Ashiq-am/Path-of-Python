import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# Setup a plot such that only the bottom
# spine is shown
def setup(ax):
    ax.spines['right'].set_color('green')
    ax.spines['left'].set_color('red')

    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines['top'].set_color('pink')
    ax.xaxis.set_ticks_position('bottom')

    ax.tick_params(which='major', width=1.00)
    ax.tick_params(which='major', length=5)
    ax.tick_params(which='minor', width=0.75)
    ax.tick_params(which='minor', length=2.5)

    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.patch.set_alpha(0.0)


plt.figure(figsize=(8, 6))
n = 8
ax = plt.subplot(n, 1, 4)
setup(ax)
ax.xaxis.set_major_locator(ticker.LinearLocator(3))
ax.xaxis.set_minor_locator(ticker.LinearLocator(31))

ax.text(0.0, 0.1, "LinearLocator",
        fontsize=14,
        transform=ax.transAxes)

plt.subplots_adjust(left=0.05,
                    right=0.95,
                    bottom=0.05,
                    top=1.05)

plt.show()
