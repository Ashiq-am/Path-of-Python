# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

fig, ax2 = plt.subplots(sharex=True)
fig.subplots_adjust(left=0.2, wspace=0.6)
box = dict(facecolor='green', pad=5, alpha=0.2)

ax2.plot(20 * np.random.rand(10))
ax2.xaxis.set_label_text('X - Label', bbox=box)
ax2.set_xlim(0, 10)
print("Text of the Label :", ax2.xaxis.get_label_text())

fig.suptitle("Matplotlib.axis.Axis.get_label_text()\
Function Example", fontsize=12, fontweight='bold')

plt.show()
