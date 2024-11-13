# ImpleIn Reviewtation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(16, 365, (365 - 16) * 4)
xdata = np.sin(2 * np.pi * t / 15)
ydata = np.cos(2 * np.pi * t / 12)

fig, (ax, ax1) = plt.subplots(1, 2)

ax.plot(xdata, ydata, 'g-', alpha=0.6)
ax.set_title("Axes 1")
ax1.plot(xdata, ydata, 'g-', alpha=0.6)
ax1.set_autoscaley_on(False)
ax1.set_title("Axes 2")

w = ax.get_autoscaley_on()
w1 = ax1.get_autoscaley_on()
ax.text(-0.5, 0, "Value return : " + str(w),
        fontweight="bold")
ax1.text(-0.5, 0.5, "Value return : " + str(w1),
         fontweight="bold")

fig.suptitle('matplotlib.axes.Axes.get_autoscaley_on() \
function Example\n', fontweight="bold")
fig.canvas.draw()
plt.show()
