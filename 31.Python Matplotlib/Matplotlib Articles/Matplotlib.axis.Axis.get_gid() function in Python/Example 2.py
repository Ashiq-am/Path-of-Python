# Implementation of matplotlib function
from matplotlib.axis import Axis
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

print("Value Return :")
for i, t in enumerate(ax.patches):
    Axis.set_gid(t, 'patch_% d' % i)
    print(Axis.get_gid(t))

for i, t in enumerate(ax.texts):
    Axis.set_gid(t, 'tooltip_% d' % i)
    print(Axis.get_gid(t))

ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect('equal')

fig.suptitle("""matplotlib.axis.Axis.get_gid() 
function Example\n""", fontweight="bold")

plt.show()
