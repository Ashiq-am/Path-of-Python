# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

d = np.arange(100).reshape(10, 10)
xx, yy = np.meshgrid(np.arange(11), np.arange(11))

fig, ax = plt.subplots()

ax.set_aspect(1)
m = ax.pcolormesh(xx, yy, d)

if Axis.get_rasterized(m) == None:
    Axis.set_rasterized(m, True)

fig.suptitle("""matplotlib.axis.Axis.get_rasterized() 
function Example\n""", fontweight="bold")

plt.show()
