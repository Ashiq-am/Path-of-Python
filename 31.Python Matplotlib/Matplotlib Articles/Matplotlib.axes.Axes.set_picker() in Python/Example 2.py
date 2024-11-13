# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

X = np.random.rand(10, 200)
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(xs, ys, 'go-')

ax.set_picker(True)

fig.suptitle('matplotlib.axes.Axes.set_picker()\
function Example', fontweight="bold")
plt.show()
