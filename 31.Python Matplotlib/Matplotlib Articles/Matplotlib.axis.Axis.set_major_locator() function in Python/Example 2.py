# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = [0, 5, 9, 10, 15]
y = [0, 1, 2, 3, 4]

tick_spacing = 1

fig, ax = plt.subplots(1, 1)
ax.plot(x, y)
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

fig.suptitle("Matplotlib.axis.Axis.set_major_locator()\n\
Function Example", fontsize=12, fontweight='bold')

plt.show()
