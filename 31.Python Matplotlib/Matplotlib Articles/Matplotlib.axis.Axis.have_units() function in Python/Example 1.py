# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt

fig, axs = plt.subplots()
axs.plot([1, 2, 3])

axs.set_title("Units are set on any axis : "
              + str(axs.xaxis.have_units()))

fig.suptitle('matplotlib.axis.Axis.have_units() \
function Example\n', fontweight="bold")

plt.show()
