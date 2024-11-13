# Implementation of matplotlib function
import numpy as np
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig, ax = plt.subplots()
ax.plot(np.random.rand(1000), 'go')

Axis.set_minor_locator(ax.yaxis, ticker.MultipleLocator(1))

print("Value of get_minorticklabels() :")
for i in ax.yaxis.get_minorticklabels():
    print(i)

plt.title("Matplotlib.axis.Axis.get_minorticklabels()\n\
Function Example", fontsize=12, fontweight='bold')

plt.show()
