# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

geeks = np.array([24.40, 110.25, 20.05,
                  22.00, 61.90, 7.80,
                  15.00, 22.80, 34.90,
                  57.30])

fig, ax = plt.subplots()
ax.acorr(geeks, maxlags=9)

ax.set_ylabel('Y-axis')
ax.start_pan(0, 0.6, 1)
ax.drag_pan(1, "shift", 0, 0.6)

ax.set_title('matplotlib.axes.Axes.drag_pan() Example')
plt.show()
