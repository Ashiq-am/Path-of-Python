# Implementation of matplotlib function
import matplotlib.pyplot as plt


def make_patch_spines_invisible(ax):
	ax.set_frame_on(True)
	ax.patch.set_visible(False)
	for sp in ax.spines.values():
		sp.set_visible(False)


fig, host = plt.subplots()
fig.subplots_adjust(right = 0.75)

par1 = host.twinx()
par2 = host.twinx()

# Offset the right spine of par2.
# The ticks and label have already been
# placed on the right by twinx above.
par2.spines["right"].set_position(("axes",
								1.2))

# Having been created by twinx, par2
# has its frame off, so the line of its
# detached spine is invisible. First,
# activate the frame but make the patch
# and spines invisible.
make_patch_spines_invisible(par2)

# Second, show the right spine.
par2.spines["right"].set_visible(True)

p1, = host.plot([0, 1, 2], [0, 1, 2], "b-",
				label ="Y-label 1")

p2, = par1.plot([0, 1, 2], [0, 30, 20],
				"r-", label ="Y-label 2")

p3, = par2.plot([0, 1, 2], [500, 300, 150],
				"g-", label ="Y-label 3")

host.set_xlim(0.25, 1.75)
host.set_ylim(0.25, 1.75)
par1.set_ylim(0, 40)
par2.set_ylim(10, 500)

host.set_xlabel("X-label")
host.set_ylabel("Y-label 1")
par1.set_ylabel("Y-label 2")
par2.set_ylabel("Y-label 3")

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())
par2.yaxis.label.set_color(p3.get_color())

tkw = dict(size = 4, width = 1.5)
host.tick_params(axis ='y',
				colors = p1.get_color(),
				**tkw)

par1.tick_params(axis ='y',
				colors = p2.get_color(),
				**tkw)

par2.tick_params(axis ='y',
				colors = p3.get_color(),
				**tkw)

host.tick_params(axis ='x', **tkw)

lines = [p1, p2, p3]

host.legend(lines, [l.get_label() for l in lines])


fig.suptitle('matplotlib.axes.Axes.tick_params() function Example\n\n', fontweight ="bold")

plt.show()
