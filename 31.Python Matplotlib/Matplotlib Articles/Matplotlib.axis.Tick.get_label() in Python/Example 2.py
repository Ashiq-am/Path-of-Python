# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


fig, host = plt.subplots()
fig.subplots_adjust(right=0.75)

par1 = host.twinx()

p1, = host.plot([0, 1, 2], [0, 1, 2],
                "g-", label="Y-label 1")
p2, = par1.plot([0, 1, 2], [0, 30, 20],
                "r-", label="Y-label 2")

host.set_xlim(0.25, 1.75)
host.set_ylim(0.25, 1.75)
par1.set_ylim(0, 40)

host.set_xlabel("X-label")
host.set_ylabel("Y-label 1")
par1.set_ylabel("Y-label 2")

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y',
                 colors=p1.get_color(),
                 **tkw)
par1.tick_params(axis='y',
                 colors=p2.get_color(),
                 **tkw)
host.tick_params(axis='x',
                 **tkw)

lines = [p1, p2]

host.legend(lines, [l.get_label() for l in lines])

fig.suptitle("""matplotlib.axis.Tick.get_label()
function Example\n""", fontweight="bold")

plt.show()
