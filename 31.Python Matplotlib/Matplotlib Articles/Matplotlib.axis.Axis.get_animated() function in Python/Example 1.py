# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = np.array([[1, 2, 3, 4, 5],
                 [7, 4, 9, 2, 3]])

fig = plt.figure()
ax = plt.axes(xlim=(0, 20), ylim=(0, 20))

line, = ax.plot([], [], 'r-')
annotation = ax.annotate('', xy=(data[0][0],
                                 data[1][0]))

Axis.set_animated(annotation, True)
w = Axis.get_animated(annotation)

print(str(w))

fig.suptitle("""matplotlib.axis.Axis.get_animated() 
function Example\n""", fontweight="bold")

plt.show()
