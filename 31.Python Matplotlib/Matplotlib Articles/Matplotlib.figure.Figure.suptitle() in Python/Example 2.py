# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

xdata = np.random.random([2, 10])

xdata1 = xdata[0, :]
xdata2 = xdata[1, :]

ydata1 = xdata1 ** 2
ydata2 = 1 - xdata2 ** 3

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, color='tab:blue')
ax.plot(xdata2, ydata2, color='tab:orange')

ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

fig.suptitle('matplotlib.figure.Figure.suptitle()\
function Example\n\n', fontweight="bold")

plt.show()
