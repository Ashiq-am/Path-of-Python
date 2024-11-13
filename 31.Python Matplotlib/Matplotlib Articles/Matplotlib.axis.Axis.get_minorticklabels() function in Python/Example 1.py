# Implementation of matplotlib function
import numpy as np
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(100 * np.random.rand(20))

Axis.set_minor_locator(ax.xaxis, ticker.MultipleLocator(1))

print("Value of get_minorticklabels() :")
for i in ax.xaxis.get_minorticklabels():
    print(i)

plt.title("Matplotlib.axis.Axis.get_minorticklabels()\n\
Function Example", fontsize=12, fontweight='bold')

plt.show()
