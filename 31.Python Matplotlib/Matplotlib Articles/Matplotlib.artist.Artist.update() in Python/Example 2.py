# Implementation of matplotlib function
from matplotlib.artist import Artist
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(-20)
prop = {'autoscalex_on': False}

Artist.update(ax, prop)

fig.suptitle('matplotlib.artist.Artist.update() \
function Example', fontweight="bold")

plt.show()
