# ImpleIn Reviewtation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 20, 300)
xdata = np.sin(np.pi * t / 12)
ydata = np.cos(4 * np.pi * t / 21)

fig, ax = plt.subplots()

ax.plot(xdata, ydata, 'g-')
ax.set_autoscaley_on(False)

fig.suptitle('matplotlib.axes.Axes.set_autoscaley_on() function Example\n', fontweight ="bold")
fig.canvas.draw()
plt.show()
