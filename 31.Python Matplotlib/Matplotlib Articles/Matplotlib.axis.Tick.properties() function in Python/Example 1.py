# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(3, 4)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(2)

w = Tick.properties(ax)
print("Display first 10 Properties\n")
for i in list(w)[:10]:
    print(i, ":", w[i])

fig.suptitle('matplotlib.axis.Tick.properties() \
function Example', fontweight="bold")

plt.show()
