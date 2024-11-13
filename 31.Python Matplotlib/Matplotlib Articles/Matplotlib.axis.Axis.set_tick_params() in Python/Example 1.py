# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.02)

fig, ax1 = plt.subplots()

ax1.plot(t, np.sin(4 * np.pi * t))
ax1.grid(True)
ax1.set_ylim((-2, 2))

ax1.xaxis.set_tick_params(labelcolor='r')
ax1.yaxis.set_tick_params(labelcolor='g')

plt.title('matplotlib.axis.Axis.set_tick_params()\n\
function Example', fontweight="bold")

plt.show()
