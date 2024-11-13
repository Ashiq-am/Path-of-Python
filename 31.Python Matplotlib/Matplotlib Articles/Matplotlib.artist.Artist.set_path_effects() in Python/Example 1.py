# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as path_effects

fig, ax = plt.subplots()
t = ax.text(0.02, 0.5,
            'GeeksForGeeks',
            fontsize=40,
            weight=1000,
            va='center')

Artist.set_path_effects(t, [path_effects.PathPatchEffect(offset=(4, -4),
                                                         hatch='xxxx',
                                                         facecolor='lightgreen'),
                            path_effects.PathPatchEffect(edgecolor='white',
                                                         linewidth=1.1,
                                                         facecolor='green')])

fig.suptitle('matplotlib.artist.Artist.set_path_effects()\
function Example', fontweight="bold")

plt.show()
