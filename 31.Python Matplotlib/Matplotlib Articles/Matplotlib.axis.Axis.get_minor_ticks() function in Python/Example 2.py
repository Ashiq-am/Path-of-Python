# Implementation of matplotlib function
import numpy as np
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(100 * np.random.rand(20))

ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

print("Value of get_minor_ticks() :")
for tick in ax.xaxis.get_minor_ticks():
    tick.label1.set_color('red')
    print(tick)

plt.title("Matplotlib.axis.Axis.get_minor_ticks()\n\
Function Example", fontsize=12, fontweight='bold')

plt.show()
