# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.set_facecolor('# E56B51')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.plot(t, s, )
ax.set_title('matplotlib.axes.Axes.get_facecolor()\
Example\n', fontsize=12, fontweight='bold')
plt.show()
