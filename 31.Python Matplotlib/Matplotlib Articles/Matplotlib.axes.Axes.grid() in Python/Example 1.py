# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1, 2, 3])
ax.grid()
ax.set_title('matplotlib.axes.Axes.grid() Example\n',
             fontsize=12, fontweight='bold')
plt.show()
