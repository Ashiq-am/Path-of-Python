# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

fig, ax2 = plt.subplots(sharex=True)
fig.subplots_adjust(left=0.2, wspace=0.6)
box = dict(facecolor='green', pad=5, alpha=0.2)

ax2.plot(20 * np.random.rand(10))
ax2.set_xlabel('X - Label', bbox=box)
ax2.set_xlim(0, 10)
Axis.set_label_coords(ax2.xaxis, 0.5, 0.95)

w = ax2.xaxis.get_minpos()

print("Value Return :\n" + str(w))

fig.suptitle("""matplotlib.axis.Axis.get_minpos() 
function Example\n""", fontweight="bold")

plt.show()
