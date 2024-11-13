# Implementation of matplotlib function
import numpy as np
from matplotlib.axis import Axis
import matplotlib.pyplot as plt

t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)

fig, ax = plt.subplots()

ax.plot(t, s)
ax.grid(True)
ax.set_ylabel('y-axis', fontweight='bold')
ax.set_xlabel('x-axis', fontweight='bold')

Axis.cla(ax.yaxis)

plt.title("Matplotlib.axis.Axis.cla()\n\
Function Example", fontsize=12, fontweight='bold')
plt.show()
