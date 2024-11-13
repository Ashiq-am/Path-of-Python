# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-5, 5, 1)
Y = np.arange(-5, 5, 1)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)

w = ax.xaxis.get_minpos()

print("Value Return :\n" + str(w))

fig.suptitle("""matplotlib.axis.Axis.get_minpos() 
function Example\n""", fontweight="bold")

plt.show()
