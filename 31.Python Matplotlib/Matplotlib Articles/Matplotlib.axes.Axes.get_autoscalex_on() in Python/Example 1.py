# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 20, 300)
xdata = np.sin(2 * np.pi * t / 12)
ydata = np.cos(4 * np.pi * t / 21)

fig, ax = plt.subplots()

ax.plot(xdata, ydata, 'g-')
ax.set_autoscalex_on(False)

w = ax.get_autoscalex_on()
ax.text(0.2, 0, "Value return by get_autoscalex_on : "
        + str(w), fontweight="bold")

fig.suptitle('matplotlib.axes.Axes.get_autoscalex_on() \
function Example\n', fontweight="bold")
fig.canvas.draw()
plt.show()
