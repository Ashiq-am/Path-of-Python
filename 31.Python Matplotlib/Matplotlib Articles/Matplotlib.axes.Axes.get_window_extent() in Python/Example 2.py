# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, ax3 = plt.subplots()

m = ax3.pcolor(xx)
m.set_zorder(-20)
w = ax3.get_window_extent()
print(str(w))

fig.suptitle('matplotlib.axes.Axes.get_window_extent() \
function Example', fontweight="bold")

plt.show()
