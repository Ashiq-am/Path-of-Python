# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

# Create some mock data
t = np.arange(0.01, 10.0, 0.001)
data1 = np.exp(t)
data2 = np.sin(0.4 * np.pi * t)

fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_ylabel('time (s)')
ax1.set_xlabel('exp', color = color)
ax1.plot(data1, t, color = color)
ax1.tick_params(axis ='x', labelcolor = color)

ax2 = ax1.twiny()

color = 'tab:green'
ax2.set_xlabel('sin', color = color)
ax2.plot(data2, t, color = color)
ax2.tick_params(axis ='x', labelcolor = color)

fig.suptitle('matplotlib.axes.Axes.twiny() function Example\n\n', fontweight ="bold")
plt.show()
