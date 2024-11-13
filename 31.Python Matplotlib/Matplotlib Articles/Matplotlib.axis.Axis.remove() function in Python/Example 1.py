# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt

fig, axs = plt.subplots()
axs.plot([1, 2, 3])

# use of remove() method
Axis.remove(axs)

fig.suptitle('matplotlib.axis.Axis.remove() \
function Example\n', fontweight="bold")

plt.show()
