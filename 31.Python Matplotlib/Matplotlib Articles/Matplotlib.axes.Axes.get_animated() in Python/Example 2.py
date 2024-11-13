# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

L = 50
theta = np.linspace(0, 2 * np.pi, L)
r = np.ones_like(theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

line, = ax.plot(1, 0, 'ro')

annotation = ax.annotate(
	'annotation', xy =(1, 0), xytext =(-1, 0),
	arrowprops = {'arrowstyle': "->"}
)
annotation.set_animated(False)

w = annotation.get_animated()

print(str(w))

fig.suptitle('matplotlib.axes.Axes.get_animated() function Example\n\n', fontweight ="bold")

plt.show()
