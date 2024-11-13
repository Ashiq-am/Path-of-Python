# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.plot([1, 2, 3])

w = ax.get_xscale()

ax.set_title("xscale property : " + str(w),
             fontweight="bold")
fig.suptitle('matplotlib.axes.Axes.get_xscale()\
function Example\n', fontweight="bold")

fig.canvas.draw()
plt.show()
