# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, [(ax1, ax2), (ax3, ax4)] = plt.subplots(2, 2)

x = np.random.randn(20, 50)
x[5, :] = 0.
x[:, 12] = 0.

ax1.spy(x, markersize = 4)
ax2.spy(x, precision = 0.2, markersize = 4)

ax3.spy(x)
ax4.spy(x, precision = 0.4)

ax1.set_title("Value Return by get_data_ratio : "
			+str(ax1.get_data_ratio())+"\n")


ax2.set_title("Value Return by get_data_ratio : "
			+str(ax2.get_data_ratio())+"\n")

ax3.set_title("Value Return by get_data_ratio : "
			+str(ax3.get_data_ratio())+"\n")

ax4.set_title("Value Return by get_data_ratio : "
			+str(ax4.get_data_ratio())+"\n")

fig.suptitle('matplotlib.axes.Axes.get_data_ratio Example')

plt.show()
