# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10 ** 7)
geeks = np.random.randn(100)

fig, ax = plt.subplots()
ax.acorr(geeks, usevlines=True,
         normed=True,
         maxlags=80, lw=3)

ax.grid(True)

prop = {'xticks': np.array([-10., -5., 0., 5., 10.]),
        'yticks': np.array([-0.2, 0.2, 0.6, 1., 1.4]),
        'ylabel': None, 'xlabel': None}

ax.update(prop)

fig.suptitle('matplotlib.axes.Axes.update()\
function Example', fontweight="bold")

plt.show()
