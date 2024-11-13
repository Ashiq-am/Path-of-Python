# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig.subplots_adjust(left=0.2, wspace=0.6)
box = dict(facecolor='green', pad=5, alpha=0.2)

np.random.seed(19680801)
ax1.plot(2 * np.random.rand(10))
ax1.set_title('Label is not aligned')
ax1.yaxis.set_label_text('Default', bbox=box)
ax1.set_ylim(0, 20)
print("Position of Label in Axes 1 :",
      ax1.yaxis.get_label_position())

ax2.set_title('\nLabel is aligned')
ax2.plot(20 * np.random.rand(10))
ax2.yaxis.set_label_text('Adjusted', bbox=box)
ax2.yaxis.set_label_position('right')
ax2.set_ylim(0, 20)
print("Position of Label in Axes 2 :",
      ax2.yaxis.get_label_position())

fig.suptitle("Matplotlib.axis.Axis.get_label_position()\
Function Example", fontsize=12, fontweight='bold')

plt.show()
