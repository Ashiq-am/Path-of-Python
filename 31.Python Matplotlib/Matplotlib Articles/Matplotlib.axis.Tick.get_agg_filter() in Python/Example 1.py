# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.artist import Artist


xx = np.random.rand(3, 4)

fig, axs = plt.subplots()

m = axs.pcolor(xx)
m.set_zorder(2)

val = Tick.get_agg_filter(axs)
axs.set_title("Value Return by get_agg_filter(): "
			+ str(val))

fig.suptitle("""matplotlib.axis.Tick.get_agg_filter()
function Example\n""", fontweight="bold")

plt.show()
