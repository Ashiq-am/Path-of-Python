# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.1, 3.0, 0.04)

fig, ax1 = plt.subplots()

ax1.plot(t, np.sin(4*np.pi * t))
ax1.grid(True)
ax1.set_ylim((-3, 3))

ax1.xaxis.set_tick_params(labelcolor='r')
ax1.yaxis.set_tick_params(labelcolor='g')

plt.title('matplotlib.axis.XAxis.set_tick_params() function Example',
		fontweight="bold")

plt.show()
