# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(-20)
prop = {'autoscalex_on': False}

Axis.update(ax, prop)

plt.title('matplotlib.axis.Axis.update() \
function Example', fontweight="bold")

plt.show()
