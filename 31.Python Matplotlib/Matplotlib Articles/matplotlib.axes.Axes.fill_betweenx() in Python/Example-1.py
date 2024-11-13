# Implementation of matplotlib function

import numpy as np
import matplotlib.pyplot as plt

y = np.arange(-5, 5, 0.01)
x1 = -y * 2 + y + 10
x2 = 2 * y + y

fig, ax = plt.subplots()
ax.plot(y, x1, y, x2, color='black')
ax.fill_betweenx(y, x1, x2, where=x2 > x1,
                 facecolor='green', alpha=0.8)

ax.fill_betweenx(y, x1, x2, where=x2 <= x1,
                 facecolor='black', alpha=0.8)

ax.set_title('matplotlib.axes.Axes.fill_betweenx Example1')
plt.show()
