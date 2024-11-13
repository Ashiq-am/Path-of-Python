# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10 ** 7)
geeks = np.random.randn(40)

fig, ax = plt.subplots()
ax.acorr(geeks, usevlines=True,
         normed=True, maxlags=9, lw=3)

ax.grid(True)

ax.xaxis.set_default_intervals()

fig.suptitle("""matplotlib.axis.Axis.set_default_intervals() 
function Example\n""", fontweight="bold")

plt.show()
