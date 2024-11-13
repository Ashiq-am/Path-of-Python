# ImpleIn Reviewtation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xdata = np.linspace(16, 365, (365-16)*4)
ydata = np.sin(2 * np.pi * xdata / 153) + np.cos(2 * np.pi * xdata / 127)

fig, (ax, ax1) = plt.subplots(1, 2)

ax.plot(xdata, ydata, 'g-')
ax1.set_autoscale_on(True)
ax.set_title("set_autoscale_on value : True")
ax1.plot(xdata, ydata, 'g-')
ax1.set_autoscale_on(False)
ax1.set_title("set_autoscale_on vale : False")

fig.suptitle('matplotlib.axes.Axes.set_autoscale_on() function Example\n', fontweight ="bold")
fig.canvas.draw()
plt.show()
