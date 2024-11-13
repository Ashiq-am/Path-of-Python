# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, (ax3, ax4) = plt.subplots(1, 2)

m = ax3.pcolor(xx)
m.set_zorder(-20)

w = ax3.get_rasterization_zorder()
ax3.set_title("Rasterization Zorder Value : " + str(w))

m = ax4.pcolor(xx)
m.set_zorder(-20)

ax4.set_rasterization_zorder(-10)
w = ax4.get_rasterization_zorder()
ax4.set_title("Rasterization Zorder Value : " + str(w))

fig.suptitle('matplotlib.axes.Axes.get_rasterization_zorder()\
function Example', fontweight="bold")

plt.show()
