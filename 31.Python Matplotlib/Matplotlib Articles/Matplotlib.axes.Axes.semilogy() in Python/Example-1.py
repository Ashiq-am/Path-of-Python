# Implementation of matplotlib function

import numpy as np
import matplotlib.pyplot as plt

test = np.arange(0.01, 30.0, 0.1)

# Create figure
fig, ax = plt.subplots()

# log x axis
ax.semilogy(test, np.exp(-test / 5.0))
ax.grid()

ax.set_title('matplotlib.axes.Axes.semilogy Example1')
plt.show()
