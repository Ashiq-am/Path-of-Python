# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

fig, ax = plt.subplots()

x, y, s, c = np.random.rand(4, 200)
s *= 200

ax.scatter(x, y, s, c)
ax.set_navigate_mode("ZOOM")

ax.set_title('matplotlib.axes.Axes.set_navigate_mode()\
function Example', fontweight="bold")

ax.grid()

plt.show()
