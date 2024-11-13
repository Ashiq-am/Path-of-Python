# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
x = np.linspace(-np.pi, np.pi, 100)
y = 2 * np.sin(x)

ax = fig.add_subplot()
ax.set_title('centered spines')
ax.plot(x, y)

ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks([-3, -2.5, -2, -1.5, -1,
                    -0.5, 0, 0.5, 1, 1.5,
                    2, 2.5, 3])

ax.grid()

fig.suptitle("""matplotlib.axis.Axis.set_ticks() 
function Example\n""", fontweight="bold")

plt.show()
