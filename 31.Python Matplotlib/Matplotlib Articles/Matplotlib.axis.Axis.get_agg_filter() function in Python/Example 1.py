# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.artist import Artist

xx = np.random.rand(6, 5)

fig, axs = plt.subplots()

m = axs.pcolor(xx)
m.set_zorder(-2)

# use of get_agg_filter() method
val = Axis.get_agg_filter(axs)
axs.set_title("Value Return by get_agg_filter(): "
              + str(val))

fig.suptitle("""matplotlib.axis.Axis.get_agg_filter() 
function Example\n""", fontweight="bold")

plt.show()
