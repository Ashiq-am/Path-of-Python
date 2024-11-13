# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1, sharex = True)
fig.subplots_adjust(left=0.2, wspace=0.6)
box = dict(facecolor='green', pad=5, alpha=0.2)

np.random.seed(19680801)
ax1.plot(2*np.random.rand(10))
ax1.set_title('Label is not aligned')
ax1.set_ylabel('Default', bbox=box)
ax1.set_ylim(0, 20)

ax2.set_title('\nLabel is aligned')
ax2.plot(20*np.random.rand(10))
ax2.set_ylabel('Adjusted', bbox=box)
ax2.set_ylim(0, 20)
Axis.set_label_coords(ax2.yaxis,1.1, 0.5)

fig.suptitle("Matplotlib.axis.Axis.set_label_coords() Function Example", fontsize = 12, fontweight ='bold')

plt.show()
