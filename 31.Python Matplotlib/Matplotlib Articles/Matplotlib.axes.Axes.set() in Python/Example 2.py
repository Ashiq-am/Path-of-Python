# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(19680801)

fig, ax = plt.subplots()

x, y, s, c = np.random.rand(4, 200)
s *= 200

ax.scatter(x, y, s, c)

ax.set(xlabel ='X-Axis', ylabel ='Y-Axis',
	xlim =(0, 0.5), ylim =(0, 0.5),
	title ='matplotlib.axes.Axes.set() function Example')
ax.grid()

plt.show()
