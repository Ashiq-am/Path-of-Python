# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt

fig, axs = plt.subplots()
axs.plot([1, 2, 3])

axs.set_title("Is artist is explicitly set transform : "
              + str(Axis.is_transform_set(axs)))

fig.suptitle('matplotlib.axis.Axis.is_transform_set() \
function Example\n', fontweight="bold")

plt.show()
