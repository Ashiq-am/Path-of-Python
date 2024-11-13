# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = np.array([[1, 2, 3, 4, 5],
				[7, 4, 9, 2, 3]])

fig = plt.figure()
ax = plt.axes(xlim=(0, 7.5), ylim=(0, 10))

line, = ax.plot(data[0], data[1], 'go-')
annotation = ax.annotate('', xy=(data[0][0],
								data[1][0]))

Tick.set_animated(annotation,
				not Tick.get_animated(annotation))

fig.suptitle("""matplotlib.axis.Tick.get_animated()
function Example\n""", fontweight="bold")

plt.show()
