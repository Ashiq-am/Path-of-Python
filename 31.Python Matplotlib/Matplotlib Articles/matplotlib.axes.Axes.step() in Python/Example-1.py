# Implementation of matplotlib function

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(16)
y = np.sin(x / 3)

fig, ax = plt.subplots()

ax.step(x, y + 2, color='green')
ax.plot(x, y + 2, 'o--', color='black', alpha=0.3)

ax.set_title('matplotlib.axes.Axes.step Example1')
plt.show()
