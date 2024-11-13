# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(-20)

w = ax.get_agg_filter()
ax.set_title("Value Return by get_agg_filter(): " + str(w))

fig.suptitle('matplotlib.axes.Axes.get_agg_filter() \
function Example', fontweight="bold")

plt.show()
