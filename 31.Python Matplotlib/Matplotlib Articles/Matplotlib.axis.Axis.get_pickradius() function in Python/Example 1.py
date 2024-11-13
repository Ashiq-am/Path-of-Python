# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

X = np.random.rand(10, 200)
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(xs, ys, 'go-')

ax.grid()

print("Value return by get_pickradius() :",
      ax.yaxis.get_pickradius())

fig.suptitle("""matplotlib.axis.Axis.get_pickradius() 
function Example\n""", fontweight="bold")

plt.show()
