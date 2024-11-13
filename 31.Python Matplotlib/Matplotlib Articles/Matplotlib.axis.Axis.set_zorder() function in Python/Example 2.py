# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(6, 5)

fig, (ax3, ax4) = plt.subplots(1, 2)

m = ax3.pcolor(xx)

ax3.set_title("No Zorder value ")

m = ax4.pcolor(xx)
Axis.set_zorder(m, -7)

ax4.set_title("Zorder Value : -7")

fig.suptitle('matplotlib.axis.Axis.set_zorder() \
function Example\n', fontweight="bold")

plt.show()
