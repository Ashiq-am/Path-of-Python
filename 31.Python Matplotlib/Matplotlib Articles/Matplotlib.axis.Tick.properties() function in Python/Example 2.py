# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10 ** 7)
geeks = np.random.randn(100)

fig, ax = plt.subplots()
ax.acorr(geeks, usevlines=True,
         normed=True,
         maxlags=25, lw=3)

ax.grid(True)

w = Tick.properties(ax)
print("Display last 10 Properties\n")
for i in list(w)[-10:]:
    print(i, ":", w[i])

fig.suptitle('matplotlib.axis.Tick.properties() \
function Example', fontweight="bold")

plt.show()
