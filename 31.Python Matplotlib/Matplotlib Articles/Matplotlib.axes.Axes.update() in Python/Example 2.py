# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(-20)
prop = {'autoscalex_on': False}
w = ax.update(prop)

fig.suptitle('matplotlib.axes.Axes.update()\
function Example', fontweight="bold")

plt.show()
