# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.artist import Artist


np.random.seed(10**7)
geeks = np.random.randn(40)

fig, axs = plt.subplots()
axs.acorr(geeks, usevlines=True, normed=True,
		maxlags=30, lw=2)

axs.grid(True)

# use of get_agg_filter() method
val = Artist.get_agg_filter(axs)
axs.set_title("Value Return by get_agg_filter(): "
			+ str(val))

fig.suptitle('matplotlib.artist.Artist.get_agg_filter() function Example', fontweight="bold")

plt.show()
