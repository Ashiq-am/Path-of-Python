# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10 ** 7)
geeks = np.random.randn(40)

fig, ax = plt.subplots()
ax.acorr(geeks, usevlines=True,
         normed=True,
         maxlags=20, lw=3)

ax.grid(True)

print("Value return by get_view_interval() :")
w = ax.xaxis.get_view_interval()
print(w)

fig.suptitle("""matplotlib.axis.Axis.get_view_interval() 
function Example\n""", fontweight="bold")

plt.show()
