# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(10**7)
geeks = np.random.randn(40)

fig, axs = plt.subplots()
axs.acorr(geeks, usevlines=True, normed=True,
		maxlags=10, lw=2)

axs.grid(True)

val = Tick.get_agg_filter(axs)
axs.set_title("Value Return by get_agg_filter(): "
			+ str(val))

fig.suptitle("""matplotlib.axis.Tick.get_agg_filter()
function Example\n""", fontweight="bold")

plt.show()
