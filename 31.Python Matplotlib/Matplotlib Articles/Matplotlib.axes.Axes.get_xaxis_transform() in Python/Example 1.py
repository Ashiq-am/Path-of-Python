# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np


t = np.arange(0.0, 5.0, 0.1)
s = np.exp(-t) + np.sin(2 * np.pi * t) + 1
nse = np.random.normal(0.0, 0.3, t.shape) * s

fig, vax = plt.subplots()

vax.plot(t, s, 'go-')
vax.vlines(t, [0], s)
vax.vlines([1, 2], 0, 1,
		transform = vax.get_xaxis_transform(),
		colors ='r')

fig.suptitle('matplotlib.axes.Axes.get_xaxis_transform() function Example', fontweight ="bold")

plt.show()
