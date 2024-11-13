# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.set_fc('# B6ABF0')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.plot([1, 2, 3], color="black")

ax.set_title('matplotlib.axes.Axes.set_fc()\
Example\n', fontsize=12, fontweight='bold')
plt.show()
