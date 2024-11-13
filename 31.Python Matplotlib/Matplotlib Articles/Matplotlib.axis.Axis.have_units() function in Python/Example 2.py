# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_adjustable("datalim")

ax1.plot([1, 3, 34, 4, 46, 3, 7, 45, 10],
         [1, 9, 27, 8, 29, 84, 78, 19, 48],
         "o-", color="green")

ax1.set_xlim(1e-1, 1e2)
ax1.set_ylim(1, 1e2)

w = Axis.have_units(ax1.yaxis)

print("Value Return by have_units() :", w)

fig.suptitle('matplotlib.axis.Axis.have_units() \
function Example\n', fontweight="bold")

plt.show()
