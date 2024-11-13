# Implementation of matplotlib function
from matplotlib.axis import Tick
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

line, = ax.plot(.9, 0, 'go-')

annotation = ax.annotate(
	'annotation', xy=(.9, 0), xytext=(-.9, 0),
	arrowprops={'arrowstyle': "->"}
)

Tick.set_animated(annotation,
				Tick.get_animated(annotation))

fig.suptitle("""matplotlib.axis.Tick.get_animated()
function Example\n""", fontweight="bold")

plt.show()
