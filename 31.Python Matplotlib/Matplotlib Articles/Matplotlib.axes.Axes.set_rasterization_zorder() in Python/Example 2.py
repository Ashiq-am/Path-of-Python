# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, (ax3, ax4) = plt.subplots(1, 2)

m = ax3.pcolor(xx)
m.set_zorder(-20)

ax3.set_title("No Rasterization")

m = ax4.pcolor(xx)
m.set_zorder(-20)

ax4.set_rasterization_zorder(-10)

ax4.set_title("Rasterization z$<-10$")

fig.suptitle('matplotlib.axes.Axes.set_rasterization_zorder() function Example', fontweight ="bold")
plt.show()
