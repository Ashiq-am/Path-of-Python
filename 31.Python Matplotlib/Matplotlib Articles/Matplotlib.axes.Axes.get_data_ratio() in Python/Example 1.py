# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax1 = plt.subplots()

x = np.random.randn(20, 50)
x[12, :] = 0.
x[:, 22] = 0.

ax1.spy(x)
ax1.set_title("Value Return by get_data_ratio : "
			+str(ax1.get_data_ratio())+"\n")

fig.suptitle('matplotlib.axes.Axes.get_data_ratio() Example')

plt.show()
