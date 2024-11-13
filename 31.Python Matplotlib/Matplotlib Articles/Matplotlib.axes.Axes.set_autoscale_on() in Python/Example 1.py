# ImpleIn Reviewtation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xdata = np.linspace(16, 365, 300)
ydata = np.sin(2 * np.pi * xdata / 15) + np.cos(2 * np.pi * xdata / 17)

fig, ax = plt.subplots()

ax.plot(xdata, ydata, 'g-')
ax.set_autoscale_on(True)

fig.suptitle('matplotlib.axes.Axes.set_autoscale_on() function Example\n', fontweight ="bold")
fig.canvas.draw()
plt.show()
