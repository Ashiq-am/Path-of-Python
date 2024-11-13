# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10 ** 7)
geeks = np.random.randn(100)

fig, ax = plt.subplots()
ax.acorr(geeks, usevlines=True, normed=True,
         maxlags=80, lw=3)

ax.grid(True)

w = ax.get_agg_filter()
ax.set_title("Value Return by get_agg_filter(): " + str(w))

fig.suptitle('matplotlib.axes.Axes.get_agg_filter()\
function Example', fontweight="bold")

plt.show()
