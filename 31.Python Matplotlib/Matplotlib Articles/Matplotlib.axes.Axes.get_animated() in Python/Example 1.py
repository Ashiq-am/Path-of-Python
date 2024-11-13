# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


data = np.array([[1, 2, 3, 4, 5],
				[7, 4, 9, 2, 3]])

fig = plt.figure()
ax = plt.axes(xlim =(0, 20), ylim =(0, 20))

line, = ax.plot([], [], 'r-')
annotation = ax.annotate('', xy =(data[0][0],
						data[1][0]))
annotation.set_animated(True)
w = annotation.get_animated()

print(str(w))

fig.suptitle('matplotlib.axes.Axes.get_animated() function Example\n\n', fontweight ="bold")

plt.show()
