# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt
from basic_units import secs

# create masked array
data = (1, 2, 3, 4, 5, 6, 7, 8)
mask = (1, 0, 1, 0, 0, 0, 1, 0)
xsecs = secs * np.ma.MaskedArray(data, mask, float)

fig, ax1 = plt.subplots()

ax1.scatter(xsecs, xsecs)
ax1.yaxis.set_units(secs)

ax1.grid()

print("Value return by get_units() :",
      ax1.yaxis.get_units())

fig.suptitle("""matplotlib.axis.Axis.get_units() 
function Example\n""", fontweight="bold")

plt.show()
