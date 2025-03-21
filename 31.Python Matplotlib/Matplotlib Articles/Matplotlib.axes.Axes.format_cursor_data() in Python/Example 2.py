# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

geeksx = np.array([24.40, 110.25, 20.05,
                   22.00, 61.90, 7.80,
                   15.00])

fig, ax = plt.subplots()
ax.plot(geeksx, 'go-')

ax.text(1, 95, "Value return by format_cursor_data():",
        fontweight="bold")

ax.text(1.3, 85, ax.format_cursor_data(geeksx))

fig.suptitle('matplotlib.axes.Axes.format_cursor_data()\
function Example', fontweight="bold")

plt.show()
