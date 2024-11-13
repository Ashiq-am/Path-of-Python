# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10 ** 7)
geeksx = np.random.randn(10)

fig, ax = plt.subplots()
ax.plot(geeksx)

ax.text(1.5, 0.85,
        "Value return by format_cursor_data():",
        fontweight="bold")

ax.text(0, 0.7,
        Axis.format_cursor_data(ax, data=geeksx))

fig.suptitle("""matplotlib.axis.Axis.format_cursor_data() 
function Example\n""", fontweight="bold")

plt.show()
