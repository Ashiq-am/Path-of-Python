# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 3.0, 0.01)
t1 = np.exp(-t) * np.cos(2 * np.pi * t)

fig, [ax1, ax2, ax3] = plt.subplots(nrows = 3)
ax1.plot(t, t1, color ="green")
ax1.text(1.1, 0.65, 'Orginal window')

ax2.margins(2, 2)
ax2.plot(t, t1, color ="green")
ax2.text(0, 2.0, 'Zoomed out')

ax3.margins(x = 0, y =-0.25)
ax3.plot(t, t1, color ="green")
ax3.text(1.2, 0.35, 'Zoomed in')

fig.suptitle('matplotlib.axes.Axes.margins() function Example\n', fontweight ="bold")
fig.canvas.draw()
plt.show()
