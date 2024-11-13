# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10 ** 7)
geeks = np.random.randn(100)

fig, ax = plt.subplots()
ax.acorr(geeks, usevlines=True,
         normed=True,
         maxlags=80, lw=3)

ax.grid(True)

prop = {'xticks': np.array([-100., -50.,
                            0., 50., 100.]),
        'yticks': np.array([-0.2, 0.2,
                            0.6, 1., 1.4]),
        'ylabel': None, 'xlabel': None}

ax.update(prop)

w = Axis.update_units(ax.xaxis, [1, 2, 3, 4, 5])
print(w)

fig.suptitle("""matplotlib.axis.Axis.update_units() 
function Example\n""", fontweight="bold")

plt.show()
