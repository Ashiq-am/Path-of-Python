# ImpleIn Reviewtation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 20, 300)
xdata = np.sin(np.pi * t / 12)
ydata = np.cos(4 * np.pi * t / 21)

fig, ax = plt.subplots()

ax.plot(xdata, ydata, 'g-')
w = ax.get_autoscaley_on()
ax.text(-0.5, -0.75, "Value return by get_autoscaley_on : "
        + str(w),
        fontweight="bold")
fig.suptitle('matplotlib.axes.Axes.get_autoscaley_on() function \
Example\n', fontweight="bold")
fig.canvas.draw()
plt.show()
