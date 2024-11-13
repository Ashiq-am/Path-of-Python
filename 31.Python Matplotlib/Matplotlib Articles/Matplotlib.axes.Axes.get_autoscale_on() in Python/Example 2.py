# ImpleIn Reviewtation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xdata = np.linspace(16, 365, (365-16))
ydata = np.sin(2 * np.pi * xdata / 50) + np.cos(2 * np.pi * xdata / 20)

fig, (ax, ax1) = plt.subplots(1, 2)

ax.plot(xdata, ydata, 'g-', alpha = 0.4)
ax.set_title("Axes 1")
ax1.plot(xdata, ydata, 'g-')
ax1.set_autoscale_on(False)
ax1.set_title("Axes 2")

w = ax.get_autoscale_on()
ax.text(75, 0, "Value return : " + str(w),
		fontweight ="bold")

w1 = ax1.get_autoscale_on()
ax1.text(0.2, 0.5, "Value return : " + str(w1),
		fontweight ="bold")

fig.suptitle('matplotlib.axes.Axes.get_autoscale_on() function Example\n', fontweight ="bold")
fig.canvas.draw()
plt.show()
