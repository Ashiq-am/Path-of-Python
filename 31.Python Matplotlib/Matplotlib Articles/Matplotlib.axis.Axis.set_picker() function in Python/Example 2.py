# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

X = np.random.rand(10, 200)
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(xs, ys, 'go-')

Axis.set_picker(ax, picker=True)

fig.suptitle('matplotlib.axis.Axis.set_picker() \
function Example\n', fontweight="bold")

plt.show()
