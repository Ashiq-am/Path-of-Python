# Implementation of matplotlib function

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(16)
y = np.sin(x / 3)

fig, ax = plt.subplots()

ax.step(x, y + 2, label='pre (default)')
ax.plot(x, y + 2, 'o--', color='black', alpha=0.3)

ax.step(x, y + 1, where='mid', label='mid')
ax.plot(x, y + 1, 'o--', color='black', alpha=0.3)

ax.step(x, y, where='post', label='post')
ax.plot(x, y, 'o--', color='black', alpha=0.3)

ax.grid(axis='x', color='0.95')
ax.legend(title='Parameter where:')
ax.set_title('matplotlib.axes.Axes.step Example2')
plt.show()
