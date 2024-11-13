# Implementation of matplotlib function
from matplotlib.artist import Artist
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

circle = plt.Circle((0, 0), 5, fc='blue')
rect = plt.Rectangle((-5, 10), 10, 5, fc='green')

ax.add_patch(circle)
ax.add_patch(rect)

circle_tip = ax.annotate('This is a blue circle.',
                         xy=(0, 0),
                         xytext=(30, -30),
                         textcoords='offset points',
                         color='w',
                         ha='left',
                         bbox=dict(boxstyle='round, pad =.5',
                                   fc=(.1, .1, .1, .92),
                                   ec=(1., 1., 1.),
                                   lw=1,
                                   zorder=1),
                         )

rect_tip = ax.annotate('This is a green rectangle.',
                       xy=(-5, 10),
                       xytext=(30, 40),
                       textcoords='offset points',
                       color='w',
                       ha='left',
                       bbox=dict(boxstyle='round, pad =.5',
                                 fc=(.1, .1, .1, .92),
                                 ec=(1., 1., 1.),
                                 lw=1,
                                 zorder=1),
                       )

for i, t in enumerate(ax.patches):
    Artist.set_gid(t, 'patch_% d' % i)

for i, t in enumerate(ax.texts):
    Artist.set_gid(t, 'tooltip_% d' % i)

ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect('equal')

fig.suptitle("""matplotlib.artist.Artist.set_gid() 
function Example""", fontweight="bold")

plt.show()
