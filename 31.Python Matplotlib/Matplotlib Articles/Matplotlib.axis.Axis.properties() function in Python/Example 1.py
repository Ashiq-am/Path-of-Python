# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(5, 7)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(2)

w = Axis.properties(ax)
print("Display all Properties\n")
for i in w:
    print(i, ":", w[i])

fig.suptitle('matplotlib.axis.Axis.properties() \
function Example\n', fontweight="bold")

plt.show()
