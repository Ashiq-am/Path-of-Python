# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt

fig, axs = plt.subplots()
axs.plot([1, 2, 3])

# use of remove() method
Tick.remove(axs)

fig.suptitle('matplotlib.axis.Tick.remove() \
function Example', fontweight="bold")

plt.show()
