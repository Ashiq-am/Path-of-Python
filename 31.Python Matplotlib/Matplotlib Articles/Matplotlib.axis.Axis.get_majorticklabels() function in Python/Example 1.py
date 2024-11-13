# Implementation of matplotlib function
import numpy as np
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(100 * np.random.rand(20))

formatter = ticker.FormatStrFormatter('%1.2f')
Axis.set_major_formatter(ax.yaxis, formatter)

print("Value of get_major_ticks() :")
for i in ax.xaxis.get_majorticklabels():
    print(i)

plt.title("Matplotlib.axis.Axis.get_majorticklabels()\n\
Function Example", fontsize=12, fontweight='bold')
plt.show()
