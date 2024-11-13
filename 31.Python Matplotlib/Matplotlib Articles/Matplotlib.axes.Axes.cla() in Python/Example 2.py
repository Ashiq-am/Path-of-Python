# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)

fig, [ax, ax1] = plt.subplots(2, 1)

ax.set_ylabel('y-axis')
ax.plot(t, s)
ax.grid(True)
ax.set_title('matplotlib.axes.Axes.cla() Example\n\n Sample Example',
             fontsize=12, fontweight='bold')

ax1.set_ylabel('y-axis')
ax1.set_xlabel('x-axis')
ax1.plot(t, s)
ax1.grid(True)
ax1.cla()
ax1.set_title('Above example with cla()\
function', fontsize=12, fontweight='bold')
plt.show()
