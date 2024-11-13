# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(6, 5)

fig, ax = plt.subplots()

ax.pcolor(xx)
ax.set_zorder(-3)

ax.set_title("Zorder Value : "
             + str(Axis.get_zorder(ax)),
             fontweight="bold")

fig.suptitle('matplotlib.axis.Axis.get_zorder() \
function Example\n', fontweight="bold")

plt.show()
