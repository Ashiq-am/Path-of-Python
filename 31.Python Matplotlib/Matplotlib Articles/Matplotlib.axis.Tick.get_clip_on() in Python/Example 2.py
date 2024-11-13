# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.transforms as mtransforms


y0 = -0.8

arrow_style = "simple, head_length = 15, \
head_width = 30, tail_width = 10"

rect_style = "simple, tail_width = 25"
line_style = "simple, tail_width = 1"

fig, ax = plt.subplots()

trans = mtransforms.blended_transform_factory(ax.transAxes,
											ax.transData)

x_tail = 0.05
x_head = 0.95
arrow1 = mpatches.FancyArrowPatch((x_tail, y0),
								(x_head, y0),
								arrowstyle=arrow_style,
								transform=trans)

Tick.set_clip_on(arrow1, False)
ax.add_patch(arrow1)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

print("Value Return by get_clip_on() : ",
	Tick.get_clip_on(arrow1))

fig.suptitle("""matplotlib.axis.Tick.get_clip_on()
function Example\n""", fontweight="bold")

plt.show()
