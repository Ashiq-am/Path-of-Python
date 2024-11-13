# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10 ** 7)
data = np.random.normal(0, 5, 100)

fig, ax1 = plt.subplots()
val = ax1.violinplot(data)

ax1.start_pan(1, 0, 3)
ax1.drag_pan(1, "shift", 0, 0.6)

ax1.set_title('matplotlib.axes.Axes.drag_pan() Example')
plt.show()
