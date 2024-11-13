# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax1 = plt.subplots()
plt.subplots_adjust(bottom=0.25)
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
delta_f = 5.0
s = a0 * np.sin(2 * np.pi * f0 * t)

ax1.plot(t, s, lw=2, color='green')
ax1.set_ymargin(0.5)

w = ax1.can_pan()

ax1.text(0.2, 7.5, "Value return by can_pan() function:",
         fontweight="bold")
ax1.text(0.47, 5.6, w, fontweight="bold")

fig.suptitle('matplotlib.axes.Axes.can_pan() function\
Example\n\n', fontweight="bold")

plt.show()
