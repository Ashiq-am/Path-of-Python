# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.transforms as mtransforms

x0 = 1.05

arrow_style = "simple, head_length = 15, \
head_width = 25, tail_width = 10"
rect_style = "simple, tail_width = 25"
line_style = "simple, tail_width = 1"

fig, ax = plt.subplots()

trans = mtransforms.blended_transform_factory(ax.transAxes,
                                              ax.transData)

y_tail = 0
y_head = 10
arrow1 = mpatches.FancyArrowPatch((x0, y_tail),
                                  (x0, y_head),
                                  arrowstyle=arrow_style,
                                  transform=trans)

Tick.set_clip_on(arrow1, b=False)
ax.add_patch(arrow1)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

fig.suptitle('matplotlib.axis.Tick.set_clip_on() \
function Example', fontweight="bold")

plt.show()
