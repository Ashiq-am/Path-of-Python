# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10 ** 7)
geeksx = np.random.randn(10)

fig, ax = plt.subplots()
ax.plot(geeksx)

ax.text(1.5, 0.85, "Value return by format_cursor_data():",
        fontweight="bold")

ax.text(0, 0.7, ax.format_cursor_data(geeksx))

fig.suptitle('matplotlib.axes.Axes.format_cursor_data() \
function Example', fontweight="bold")

plt.show()
