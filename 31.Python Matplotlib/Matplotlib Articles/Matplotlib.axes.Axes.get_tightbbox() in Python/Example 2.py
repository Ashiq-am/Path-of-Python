# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(-20)
w = ax.get_tightbbox(fig.canvas.get_renderer(),
                     call_axes_locator=True,
                     bbox_extra_artists=None)

ax.set_title("Value Return :\n" + str(w),
             fontsize=10)

fig.suptitle('matplotlib.axes.Axes.get_tightbbox()\
function Example', fontweight="bold")

plt.show()
