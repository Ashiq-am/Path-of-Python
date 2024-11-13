# ImpleIn Reviewtation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(16, 365, (365-16)*4)
xdata = np.sin(2 * np.pi * t / 15)
ydata = np.cos(2 * np.pi * t / 12)

fig, (ax, ax1) = plt.subplots(1, 2)

ax.plot(xdata, ydata, 'g-')
ax1.set_autoscalex_on(True)
ax.set_title("set_autoscalex_on value : True")
ax1.plot(xdata, ydata, 'g-')
ax1.set_autoscalex_on(False)
ax1.set_title("set_autoscalex_on vale : False")

fig.suptitle('matplotlib.axes.Axes.set_autoscalex_on() function Example\n', fontweight ="bold")
fig.canvas.draw()
plt.show()
