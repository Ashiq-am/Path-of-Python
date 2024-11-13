# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

fig, (ax, ax1) = plt.subplots(1, 2)
t = 3 * (np.random.rand(2, 100) - .5)
x = np.cos(2 * np.pi * t)
y = np.sin(2 * np.pi * t)

ax.plot(x, y, 'g')
lower, upper = ax.get_ybound()
ax.set_title('Original Window',
             fontsize=10, fontweight='bold')

ax1.plot(x, y, 'g')
ax1.set_ybound(1.5 * lower, 0.5 * upper)
ax1.set_title('Using get_ybound() function',
              fontsize=10, fontweight='bold')
fig.suptitle('matplotlib.axes.Axes.get_ybound() Example\n',
             fontsize=14, fontweight='bold')
plt.show()
