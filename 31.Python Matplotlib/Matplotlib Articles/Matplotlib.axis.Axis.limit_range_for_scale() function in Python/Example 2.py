# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

fig, ax4 = plt.subplots()

x = 10.0 ** np.linspace(0.0, 2.0, 15)
y = x ** 2.0
ax4.set_xscale("log", nonposx='clip')
ax4.set_yscale("log", nonposy='clip')

ax4.errorbar(x, y, xerr=0.1 * x,
             yerr=2.0 + 1.75 * y,
             color="green")

ax4.set_ylim(bottom=0.1)

ax4.xaxis.limit_range_for_scale(0, 5)
ax4.yaxis.limit_range_for_scale(3, 5)

ax4.grid()

fig.suptitle("""matplotlib.axis.Axis.limit_range_for_scale() 
function Example\n""", fontweight="bold")

plt.show()
