# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

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

ax.grid()

print("Value return by get_smart_bounds() : [",
      ax.xaxis.get_smart_bounds(),
      ax.yaxis.get_smart_bounds(), "]")

fig.suptitle("""matplotlib.axis.Axis.get_smart_bounds() 
function Example\n""", fontweight="bold")

plt.show()
