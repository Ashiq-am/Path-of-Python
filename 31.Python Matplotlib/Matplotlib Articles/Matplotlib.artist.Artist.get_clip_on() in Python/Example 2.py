# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.transforms as mtransforms

x0 = -0.1

arrow_style = "simple, head_length = 15, \
head_width = 30, tail_width = 10"

rect_style = "simple, tail_width = 25"
line_style = "simple, tail_width = 1"

fig, ax = plt.subplots()

trans = mtransforms.blended_transform_factory(ax.transAxes,
                                              ax.transData)

y_tail = 5
y_head = 15
arrow1 = mpatches.FancyArrowPatch((x0, y_tail),
                                  (x0, y_head),
                                  arrowstyle=arrow_style,
                                  transform=trans)

Artist.set_clip_on(arrow1, False)
ax.add_patch(arrow1)

ax.set_xlim(0, 30)
ax.set_ylim(0, 80)

print("Value Return by get_clip_on() : ",
      Artist.get_clip_on(arrow1))

fig.suptitle('matplotlib.artist.Artist.get_clip_on()\
function Example', fontweight="bold")

plt.show()
