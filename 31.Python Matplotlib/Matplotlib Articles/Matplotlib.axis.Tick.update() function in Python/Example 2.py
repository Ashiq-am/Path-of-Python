# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(6, 5)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(-20)
prop = {'autoscalex_on': False}

Tick.update(ax, prop)

ax.set_title('matplotlib.axis.Tick.update() \
function Example', fontweight="bold")

plt.show()
