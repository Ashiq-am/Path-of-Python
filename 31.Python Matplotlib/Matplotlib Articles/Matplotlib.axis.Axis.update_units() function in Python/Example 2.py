# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(-20)

w = Axis.update_units(ax.xaxis, [1, 2, 3, 4, 5])
print(w)

fig.suptitle("""matplotlib.axis.Axis.update_units() 
function Example\n""", fontweight="bold")

plt.show()
