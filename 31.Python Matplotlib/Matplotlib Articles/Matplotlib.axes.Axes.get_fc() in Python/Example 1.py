# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_fc('# B6ABF0')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.plot([1, 2, 3], color="black")

x = ax.get_fc()
ax.text(0, 3.15, "Facecolor : " + str(x),
        style='italic', fontsize=10,
        color="green")
ax.set_title('matplotlib.axes.Axes.set_fc() \
Example\n', fontsize=12, fontweight='bold')
plt.show()
