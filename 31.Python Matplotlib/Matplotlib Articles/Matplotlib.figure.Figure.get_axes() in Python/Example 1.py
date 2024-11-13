# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
from matplotlib.patches import Polygon
import numpy as np

xs = list([1, 2, 3, 4, 5, 6, 7, 8, 9])
ys = list([9, 8, 7, 6, 5, 4, 3, 2, 1])

fig = plt.figure()

ax = fig.add_subplot(111)
ax.plot(ys, xs)

fig.get_axes()[0].set_ylabel("Y label")
fig.get_axes()[0].set_xlabel("X label")

fig.suptitle('matplotlib.figure.Figure.get_axes()\
function Example\n\n', fontweight="bold")

plt.show()
