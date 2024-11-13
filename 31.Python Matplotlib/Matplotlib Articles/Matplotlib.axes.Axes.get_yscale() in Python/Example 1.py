# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.plot([1, 2, 3])

w = ax.get_yscale()

ax.set_title("yscale property : " + str(w),
             fontweight="bold")
fig.suptitle('matplotlib.axes.Axes.get_yscale() \
function Example\n', fontweight="bold")
fig.canvas.draw()
plt.show()
