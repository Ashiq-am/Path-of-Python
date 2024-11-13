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

print("Value return by get_data_interval() :")
w = ax.xaxis.get_data_interval()
print(w)

fig.suptitle("""matplotlib.axis.Axis.get_data_interval() 
function Example\n""", fontweight="bold")

plt.show()
