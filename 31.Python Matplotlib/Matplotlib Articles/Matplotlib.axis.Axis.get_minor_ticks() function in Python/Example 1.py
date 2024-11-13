# Implementation of matplotlib function
import numpy as np
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(100 * np.random.rand(20))

formatter = ticker.FormatStrFormatter('%1.2f')
Axis.set_minor_formatter(ax.yaxis, formatter)

print("Value of get_minor_ticks() :")
for tick in ax.yaxis.get_minor_ticks(2):
    tick.label1.set_color('green')
    print(tick)

plt.title("Matplotlib.axis.Axis.get_minor_ticks()\n\
Function Example", fontsize=12, fontweight='bold')

plt.show()
