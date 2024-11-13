# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_yscale("log")
ax.set_adjustable("datalim")
ax.plot([1, 3, 10], [1, 9, 100], "o-", color="green")
ax.set_aspect(1)

ax.xaxis.limit_range_for_scale(0, 5)

ax.grid()

fig.suptitle("""matplotlib.axis.Axis.limit_range_for_scale() 
function Example\n""", fontweight="bold")

plt.show()
