# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.artist import Artist


xx = np.random.rand(16, 30)

fig, axs = plt.subplots()

m = axs.pcolor(xx)
m.set_zorder(-20)

# use of get_agg_filter() method
val = Artist.get_agg_filter(axs)
axs.set_title("Value Return by get_agg_filter(): "
			+ str(val))

fig.suptitle('matplotlib.artist.Artist.get_agg_filter() function Example', fontweight="bold")

plt.show()
