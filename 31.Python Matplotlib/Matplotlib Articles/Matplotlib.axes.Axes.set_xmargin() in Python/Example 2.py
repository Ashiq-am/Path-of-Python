# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 3, 1)
t1 = np.cos(np.pi * t) + np.sin(np.pi * t)

fig, [ax1, ax2, ax3] = plt.subplots(nrows = 3)
ax1.plot(t1, color ="green")
ax1.text(0.75, 0.65, 'Orginal window')

ax2.set_xmargin(2)
ax2.plot(t1, color ="green")
ax2.text(3, 0, 'Zoomed out')

ax3.set_xmargin(-0.45)
ax3.plot(t1, color ="green")
ax3.text(0.98, 0.45, 'Zoomed in')

fig.suptitle('matplotlib.axes.Axes.set_xmargin() function Example\n', fontweight ="bold")
fig.canvas.draw()
plt.show()
