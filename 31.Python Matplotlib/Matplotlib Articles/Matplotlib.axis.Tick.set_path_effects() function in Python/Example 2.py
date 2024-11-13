# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import numpy as np

fig, ax1 = plt.subplots()
ax1.imshow([[1, 2], [2, 3]])

txt = ax1.annotate("Fourth Qaud",
                   (1., 1.),
                   (0., 0),
                   arrowprops=dict(arrowstyle="->",
                                   connectionstyle="angle3",
                                   lw=2),
                   size=20, ha="center",
                   path_effects=[PathEffects.withStroke(linewidth=3,
                                                        foreground="r")])

Tick.set_path_effects(txt.arrow_patch, [
    PathEffects.Stroke(linewidth=5,
                       foreground="r"),
    PathEffects.Normal()])

ax1.grid(True, linestyle="-")

pe = [PathEffects.withStroke(linewidth=3,
                             foreground="r")]

for l in ax1.get_xgridlines() + ax1.get_ygridlines():
    Tick.set_path_effects(l, pe)

fig.suptitle('matplotlib.axis.Tick.set_path_effects() \
function Example', fontweight="bold")

plt.show()
