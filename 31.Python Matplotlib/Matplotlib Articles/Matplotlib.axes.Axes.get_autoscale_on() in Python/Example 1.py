# ImpleIn Reviewtation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xdata = np.linspace(16, 365, 300)
ydata = np.sin(2 * np.pi * xdata / 15) + np.cos(2 * np.pi * xdata / 17)

fig, ax = plt.subplots()

ax.plot(xdata, ydata, 'g-')

w = ax.get_autoscale_on()
ax.text(75, 1.95, "Value return by get_autoscale_on : "
		+ str(w), fontweight ="bold")

fig.suptitle('matplotlib.axes.Axes.get_autoscale_on() function Example\n', fontweight ="bold")
fig.canvas.draw()
plt.show()
