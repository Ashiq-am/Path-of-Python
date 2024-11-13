# Implementation of matplotlib function

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

dt = 0.1
test = np.arange(dt, 30.0, dt)

ax.semilogx(test, np.exp(-test / 6.0))
ax.grid()

ax.set_title('matplotlib.axes.Axes.semilogx Example1')
plt.show()
