# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(6, 5)

fig, (ax3, ax4) = plt.subplots(1, 2)

m = ax3.pcolor(xx)

ax3.set_title("No Zorder value ")

m = ax4.pcolor(xx)
Tick.set_zorder(m, 5)

ax4.set_title("Zorder Value : 5")

fig.suptitle('matplotlib.axis.Tick.set_zorder() \
function Example', fontweight="bold")

plt.show()
